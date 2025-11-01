FROM python:3.11-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential nginx \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY pyproject.toml ./
COPY app ./app
COPY agents ./agents
COPY configs ./configs
COPY schemas ./schemas
COPY src ./src
COPY observability.py ./observability.py

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -e . \
    && pip install --no-cache-dir streamlit faiss-cpu gunicorn uvicorn boto3

ENV VECTOR_BACKEND=faiss \
    STREAMLIT_DOCS_DIR=/data/docs \
    STREAMLIT_INDEX_DIR=/data/vector_index \
    FAISS_S3_BUCKET= \
    FAISS_S3_KEY= \
    FAISS_S3_CHECKPOINT_SEC=3600 \
    STREAMLIT_SERVER_ENABLE_CORS=false \
    STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION=false \
    STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

EXPOSE 8000 8501

COPY docker/nginx.conf /etc/nginx/nginx.conf
COPY docker/start.sh /app/start.sh
RUN chmod +x /app/start.sh

CMD ["/app/start.sh"]
