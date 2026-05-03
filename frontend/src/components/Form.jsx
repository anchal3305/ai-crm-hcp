export default function Form({ data }) {
  return (
    <div style={formContainer}>
      <Field label="Doctor Name" value={data?.doctor_name} />
      <Field label="Interaction Type" value={data?.interaction_type} />
      <Field label="Topics Discussed" value={data?.topics} />

      <Divider />

      <Field label="Sentiment" value={data?.sentiment} />
      <Field label="Outcomes" value={data?.outcomes} />
      <Field label="Follow Up" value={data?.follow_up} />
    </div>
  );
}

function Field({ label, value }) {
  return (
    <div>
      <label>{label}</label>
      <input
        value={value || ""}
        readOnly
        disabled={!value}
        style={inputStyle}
      />
    </div>
  );
}

function Divider() {
  return <hr style={{ border: "none", borderTop: "1px solid #eee" }} />;
}

const formContainer = {
  display: "flex",
  flexDirection: "column",
  gap: "18px",
};

const inputStyle = {
  width: "100%",
  padding: "10px",
  marginTop: "6px",
  borderRadius: "8px",
  border: "1px solid #d1d5db",
  backgroundColor: "#ffffff",
  fontWeight: "500",
};