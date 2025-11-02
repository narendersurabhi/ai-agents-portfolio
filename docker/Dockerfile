FROM public.ecr.aws/docker/library/python:3.11-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY pyproject.toml ./
COPY app ./app
COPY agents ./agents
COPY configs ./configs
COPY schemas ./schemas
COPY src ./src
COPY web ./web
COPY observability.py ./observability.py

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -e . \
    && pip install --no-cache-dir faiss-cpu gunicorn uvicorn boto3

ENV VECTOR_BACKEND=faiss \
    STREAMLIT_DOCS_DIR=/data/docs \
    STREAMLIT_INDEX_DIR=/data/vector_index \
    FAISS_S3_BUCKET= \
    FAISS_S3_KEY= \
    FAISS_S3_CHECKPOINT_SEC=3600

EXPOSE 8000

COPY docker/start.sh /app/start.sh
RUN chmod +x /app/start.sh

CMD ["/app/start.sh"]
