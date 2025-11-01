#!/bin/bash
set -euo pipefail

mkdir -p /data/docs /data/vector_index

if [[ -n "${FAISS_S3_BUCKET:-}" ]]; then
  python - <<'PY'
import os
import boto3
from botocore.exceptions import ClientError

bucket = os.getenv("FAISS_S3_BUCKET")
if bucket:
    s3 = boto3.client("s3")
    try:
        s3.head_bucket(Bucket=bucket)
    except ClientError as exc:
        code = exc.response.get("Error", {}).get("Code", "")
        if code in {"404", "NoSuchBucket", "NotFound"}:
            region = os.getenv("AWS_REGION") or s3.meta.region_name or "us-east-1"
            params = {"Bucket": bucket}
            if region != "us-east-1":
                params["CreateBucketConfiguration"] = {"LocationConstraint": region}
            s3.create_bucket(**params)
        else:
            raise
PY
fi

# Launch services behind nginx reverse proxy.
cleanup() {
  [[ -n "${STREAMLIT_PID:-}" ]] && kill "${STREAMLIT_PID}" 2>/dev/null || true
  [[ -n "${API_PID:-}" ]] && kill "${API_PID}" 2>/dev/null || true
}
trap cleanup EXIT INT TERM

uvicorn src.app.api:app --host 0.0.0.0 --port 8001 &
API_PID=$!

streamlit run src/app/app.py --server.port 8501 --server.address 0.0.0.0 &
STREAMLIT_PID=$!

nginx -g "daemon off;" -c /etc/nginx/nginx.conf
