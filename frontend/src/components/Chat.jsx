import { useState } from "react";
import axios from "axios";

export default function Chat({ setData }) {
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const sendMessage = async () => {
    if (!input.trim()) return;

    setLoading(true);
    setError("");

    try {
      const response = await axios.post(
        `http://127.0.0.1:8000/chat?input_text=${encodeURIComponent(input)}`
      );

      setData(response.data.data);
      setInput("");
    } catch (err) {
      console.error(err);
      setError("Failed to connect to backend");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={containerStyle}>
      <textarea
        placeholder="Describe interaction (e.g., Met Dr. Mehta, discussed insulin...)"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        style={textareaStyle}
      />

      <button onClick={sendMessage} disabled={loading} style={buttonStyle}>
        {loading ? "Processing..." : "Send"}
      </button>

      {error && <p style={{ color: "red", fontSize: "13px" }}>{error}</p>}

      <p style={helperTextStyle}>
        AI will automatically extract details and fill the form.
      </p>
    </div>
  );
}

/* ---------- Styles ---------- */

const containerStyle = {
  display: "flex",
  flexDirection: "column",
  gap: "12px",
};

const textareaStyle = {
  width: "100%",
  height: "130px",
  padding: "10px",
  borderRadius: "8px",
  border: "1px solid #d1d5db",
};

const buttonStyle = {
  alignSelf: "flex-start",
  padding: "10px 18px",
  borderRadius: "6px",
  border: "none",
  backgroundColor: "#22c55e",
  color: "#fff",
  fontWeight: "500",
  cursor: "pointer",
};

const helperTextStyle = {
  fontSize: "12px",
  color: "#6b7280",
};