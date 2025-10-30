from __future__ import annotations

import hashlib
import json
import os
from typing import Any, Dict, List


def _hash_identifier(*parts: str) -> str:
    digest = hashlib.sha256("::".join(parts).encode("utf-8")).hexdigest()[:16]
    return digest


def rules_eval(claim: Dict[str, Any]) -> Dict[str, Any]:
    """Simple synthetic rule engine over claim lines."""

    signals: List[str] = []
    score = 0.0
    for line in claim.get("lines", []):
        units = float(line.get("units", 0))
        charge = float(line.get("charge", 0))
        if units > 10:
            signals.append(f"High units for CPT {line.get('cpt')}")
            score += 0.2
        if charge > 1000:
            signals.append(f"High charge for CPT {line.get('cpt')}")
            score += 0.15
        if any(dx.startswith("Z") for dx in line.get("dx", [])):
            signals.append(f"Preventive modifier for CPT {line.get('cpt')}")
            score += 0.05
    score = min(score, 1.0)
    return {"score": round(score, 3), "signals": signals}


def feature_stats(claim_id: str) -> Dict[str, Any]:
    seed = int(_hash_identifier(claim_id), 16)
    deviation = (seed % 100) / 100 - 0.5
    return {"z_scores": {"units": round(deviation, 3), "charge": round(-deviation, 3)}}


def provider_history(npi: str) -> Dict[str, Any]:
    flags = []
    if int(npi[-1]) % 2 == 0:
        flags.append("Peer z-score above 2.5")
    if npi.startswith("99"):
        flags.append("Recent SIU referral")
    return {"flags": flags}


def search_policy(query: str) -> Dict[str, Any]:
    return {
        "hits": [
            {"uri": "policy://billing/orthopedic", "text": f"Policy guidance for {query}"},
        ]
    }


def search_claims(query: str) -> Dict[str, Any]:
    return {
        "matches": [
            {"claim_id": f"CLM-{_hash_identifier(query)[:6]}", "similarity": 0.82},
        ]
    }


def provider_graph(npi: str) -> Dict[str, Any]:
    return {
        "peers": [
            {"npi": f"{npi[:-2]}{i:02d}", "shared_members": i * 3} for i in range(1, 3)
        ]
    }


def render_pdf(document: Dict[str, Any]) -> Dict[str, Any]:
    bucket = os.environ.get("REPORT_BUCKET", "synthetic-reports")
    key = f"reports/{document.get('claim_id', 'unknown')}-{_hash_identifier(json.dumps(document, sort_keys=True))}.pdf"
    return {"report_url": f"s3://{bucket}/{key}"}


def s3_put(bucket: str, key: str, body: bytes, *, client: Any | None = None) -> Dict[str, Any]:
    if client:
        client.put_object(Bucket=bucket, Key=key, Body=body)
    size = len(body)
    return {"bucket": bucket, "key": key, "size": size}


def s3_get(bucket: str, key: str, *, client: Any | None = None) -> Dict[str, Any]:
    if client:
        response = client.get_object(Bucket=bucket, Key=key)
        content = response.get("Body", b"")
        if hasattr(content, "read"):
            content = content.read()
        return {"bucket": bucket, "key": key, "body": content}
    return {"bucket": bucket, "key": key, "body": b""}


__all__ = [
    "rules_eval",
    "feature_stats",
    "provider_history",
    "search_policy",
    "search_claims",
    "provider_graph",
    "render_pdf",
    "s3_put",
    "s3_get",
]
