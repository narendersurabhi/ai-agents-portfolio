import json
from pathlib import Path

import jsonschema


SCHEMA_DIR = Path("schemas")


def load_schema(name: str) -> dict:
    with (SCHEMA_DIR / name).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def test_claim_schema_accepts_sample():
    schema = load_schema("claim.json")
    sample = {
        "id": "CLM-1",
        "member": {"id": "M-1", "dob": "1980-01-01", "plan_id": "P-1"},
        "provider": {"npi": "1234567890", "name": "Clinic"},
        "dos": "2024-01-01",
        "place": "office",
        "amount": 100.0,
        "lines": [
            {"cpt": "99213", "units": 1, "charge": 100.0, "dx": ["Z00.00"]}
        ],
    }
    jsonschema.validate(sample, schema)


def test_triage_result_schema_accepts_sample():
    schema = load_schema("triage_result.json")
    sample = {
        "claim_id": "CLM-1",
        "risk_score": 0.5,
        "signals": ["High units"],
        "action": "manual_review",
    }
    jsonschema.validate(sample, schema)


def test_investigation_schema_accepts_sample():
    schema = load_schema("investigation.json")
    sample = {
        "claim_id": "CLM-1",
        "suspicions": ["Upcoding"],
        "evidence": [{"source": "rules_eval", "snippet": "Units exceed threshold"}],
        "peer_stats": {"units": 2.5},
    }
    jsonschema.validate(sample, schema)


def test_explanation_schema_accepts_sample():
    schema = load_schema("explanation.json")
    sample = {
        "claim_id": "CLM-1",
        "summary": "This is a sufficiently detailed summary explaining findings in depth.",
        "recommendation": "manual_review",
        "citations": ["policy://billing"],
        "report_url": "s3://bucket/report.pdf",
    }
    jsonschema.validate(sample, schema)
