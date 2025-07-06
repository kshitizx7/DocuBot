const API_BASE = "http://127.0.0.1:8000";  // Update if hosted differently
console.log("script.js loaded!");
async function uploadFile() {
  const fileInput = document.getElementById("pdfFile");
  const file = fileInput.files[0];
  if (!file) return alert("Please select a PDF file.");

  const formData = new FormData();
  formData.append("file", file);

  try {
    const res = await fetch(`${API_BASE}/upload`, {
      method: "POST",
      body: formData,
    });

    console.log("Status:", res.status);
    console.log("Headers:", res.headers.get("content-type"));

    const contentType = res.headers.get("content-type");

    let message = "";
    if (contentType && contentType.includes("application/json")) {
      const result = await res.json();
      console.log("Parsed JSON result:", result);
      message = result.message || result.detail || "Upload succeeded.";
    } else {
      const raw = await res.text();
      console.log("Non-JSON response body:", raw);
      message = raw || "Upload succeeded.";
    }

    document.getElementById("uploadStatus").textContent = message;
  } catch (err) {
    console.error("Upload error:", err);
    document.getElementById("uploadStatus").textContent = "Upload failed.";
  }
}



async function askQuestion() {
  const question = document.getElementById("question").value;
  if (!question.trim()) return alert("Please enter a question.");

  const res = await fetch(`${API_BASE}/query`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question })
  });

  const data = await res.json();
  if (res.ok) {
    document.getElementById("answer").textContent = data.answer;
    document.getElementById("sources").textContent = JSON.stringify(data.sources);
  } else {
    document.getElementById("answer").textContent = `Error: ${data.detail}`;
    document.getElementById("sources").textContent = "";
  }
}
