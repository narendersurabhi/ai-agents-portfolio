FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml ./
RUN pip install --no-cache-dir uv pipx && pipx install uv
COPY . .
RUN pip install -e .
ENV PORT=8080
CMD ["uvicorn","src.app.api:app","--host","0.0.0.0","--port","8080"]
