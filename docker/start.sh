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

# Start FastAPI (prefect concurrency via uvicorn) in background
uvicorn src.app.api:app --host 0.0.0.0 --port 8000 &
API_PID=$!

# Run Streamlit in foreground
streamlit run src/app/app.py --server.port 8501 --server.address 0.0.0.0

kill $API_PID
