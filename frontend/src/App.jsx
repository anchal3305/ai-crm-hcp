import Chat from "./components/Chat";
import Form from "./components/Form";
import { useState } from "react";

function App() {
  const [data, setData] = useState(null);

  return (
    <div style={appContainer}>
      
      {/* LEFT PANEL */}
      <div style={cardStyle}>
        <h2 style={headingStyle}>Log Interaction</h2>
        <Form data={data} />

        {/* 🔥 RESET BUTTON */}
        <button onClick={() => setData(null)} style={resetButton}>
          New Entry
        </button>
      </div>

      {/* RIGHT PANEL */}
      <div style={cardStyle}>
        <h2 style={headingStyle}>AI Assistant</h2>
        <Chat setData={setData} />
      </div>

    </div>
  );
}

export default App;

/* ---------- Styles ---------- */

const appContainer = {
  display: "flex",
  height: "100vh",
  padding: "20px",
  gap: "20px",
  backgroundColor: "#f4f6f8",
};

const cardStyle = {
  flex: 1,
  backgroundColor: "#fff",
  borderRadius: "10px",
  padding: "20px",
  boxShadow: "0 4px 12px rgba(0,0,0,0.06)",
};

const headingStyle = {
  marginBottom: "15px",
  fontWeight: "600",
};

const resetButton = {
  marginTop: "10px",
  backgroundColor: "#e5e7eb",
  color: "#111",
  border: "none",
  padding: "8px 12px",
  borderRadius: "6px",
  cursor: "pointer",
};