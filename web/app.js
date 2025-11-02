const uploadBtn = document.getElementById("upload-btn");
const reindexBtn = document.getElementById("reindex-btn");
const queryBtn = document.getElementById("query-btn");

const fileInput = document.getElementById("file-input");
const topkInput = document.getElementById("topk-input");
const questionInput = document.getElementById("question-input");

const uploadStatus = document.getElementById("upload-status");
const reindexStatus = document.getElementById("reindex-status");
const queryStatus = document.getElementById("query-status");

const resultPanel = document.getElementById("result");
const answerBlock = document.getElementById("answer");
const sourcesBlock = document.getElementById("sources");
const hitsBlock = document.getElementById("hits");
const debugBlock = document.getElementById("debug");

const API_BASE = "/api/rag";

function setStatus(el, message, type = "") {
  el.textContent = message;
  el.classList.remove("error", "success");
  if (type) {
    el.classList.add(type);
  }
}

async function uploadDocuments() {
  const files = fileInput.files;
  if (!files || files.length === 0) {
    setStatus(uploadStatus, "Select at least one document to upload.", "error");
    return;
  }

  const formData = new FormData();
  Array.from(files).forEach((file) => formData.append("files", file));

  setStatus(uploadStatus, "Uploading documents…");
  uploadBtn.disabled = true;

  try {
    const resp = await fetch(`${API_BASE}/documents`, {
      method: "POST",
      body: formData,
    });
    if (!resp.ok) {
      const detail = await resp.json().catch(() => ({}));
      throw new Error(detail.detail || "Upload failed");
    }
    const data = await resp.json();
    setStatus(
      uploadStatus,
      `Uploaded ${data.saved} document${data.saved === 1 ? "" : "s"}.`,
      "success"
    );
    fileInput.value = "";
  } catch (err) {
    setStatus(uploadStatus, err.message || "Upload failed.", "error");
  } finally {
    uploadBtn.disabled = false;
  }
}

async function rebuildIndex() {
  setStatus(reindexStatus, "Rebuilding index…");
  reindexBtn.disabled = true;
  try {
    const resp = await fetch(`${API_BASE}/reindex`, { method: "POST" });
    if (!resp.ok) {
      const detail = await resp.json().catch(() => ({}));
      throw new Error(detail.detail || "Index rebuild failed");
    }
    setStatus(reindexStatus, "Index rebuild complete.", "success");
  } catch (err) {
    setStatus(reindexStatus, err.message || "Index rebuild failed.", "error");
  } finally {
    reindexBtn.disabled = false;
  }
}

function renderResult(data) {
  if (!data) {
    resultPanel.hidden = true;
    return;
  }

  answerBlock.textContent = data.answer || "No answer returned.";

  sourcesBlock.innerHTML = "";
  const debugList = [];
  if (Array.isArray(data.sources) && data.sources.length) {
    const list = document.createElement("ul");
    data.sources.forEach((src) => {
      const item = document.createElement("li");
      item.textContent = src;
      list.appendChild(item);
    });
    const heading = document.createElement("h4");
    heading.textContent = "Sources";
    sourcesBlock.appendChild(heading);
    sourcesBlock.appendChild(list);
  }

  hitsBlock.innerHTML = "";
  if (Array.isArray(data.hits) && data.hits.length) {
    const list = document.createElement("ul");
    data.hits.forEach((hit) => {
      const item = document.createElement("li");
      const score =
        typeof hit.score === "number" ? hit.score.toFixed(3) : "n/a";
      const id = hit.id ?? "unknown";
      const chunk = hit.chunk ?? "n/a";
      item.innerHTML = `<strong>${id}</strong> · chunk ${chunk} · score ${score}`;
      list.appendChild(item);
      debugList.push({ id, chunk, score });
    });
    const heading = document.createElement("h4");
    heading.textContent = "Retrieved Chunks";
    hitsBlock.appendChild(heading);
    hitsBlock.appendChild(list);
  }

  if (debugBlock) {
    if (debugList.length) {
      debugBlock.textContent = JSON.stringify(debugList, null, 2);
      debugBlock.parentElement.hidden = false;
    } else {
      debugBlock.parentElement.hidden = true;
    }
  }

  resultPanel.hidden = false;
}

async function runQuery() {
  const question = questionInput.value.trim();
  if (!question) {
    setStatus(queryStatus, "Enter a question before running retrieval.", "error");
    resultPanel.hidden = true;
    return;
  }

  let topkValue = parseInt(topkInput.value, 10);
  if (Number.isNaN(topkValue)) {
    topkValue = 4;
  }
  topkValue = Math.min(Math.max(topkValue, 1), 20);

  setStatus(queryStatus, "Running retrieval…");
  queryBtn.disabled = true;

  try {
    const resp = await fetch(`${API_BASE}/query`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question, top_k: topkValue }),
    });
    if (!resp.ok) {
      const detail = await resp.json().catch(() => ({}));
      throw new Error(detail.detail || "Retrieval failed");
    }
    const data = await resp.json();
    renderResult(data);
    setStatus(queryStatus, "Retrieval complete.", "success");
  } catch (err) {
    renderResult(null);
    setStatus(queryStatus, err.message || "Retrieval failed.", "error");
  } finally {
    queryBtn.disabled = false;
  }
}

uploadBtn.addEventListener("click", uploadDocuments);
reindexBtn.addEventListener("click", rebuildIndex);
queryBtn.addEventListener("click", runQuery);

questionInput.addEventListener("keydown", (event) => {
  if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === "enter") {
    runQuery();
  }
});
