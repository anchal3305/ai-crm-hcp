from fastapi import FastAPI, HTTPException
from langgraph_agent import app
from db import SessionLocal, Base, engine
from models import Interaction
from fastapi.middleware.cors import CORSMiddleware

# Create tables
Base.metadata.create_all(bind=engine)

app_api = FastAPI()

# CORS
app_api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app_api.post("/chat")
async def chat(input_text: str):
    db = SessionLocal()

    try:
        # Run AI agent
        result = app.invoke({"input": input_text})

        # Extract data
        data = result.get("output", {}) or {}

        # FOLLOW-UP FIX
        if not data.get("follow_up"):
            data["follow_up"] = "Schedule next meeting"

        # Save to DB
        new_interaction = Interaction(
            doctor_name=data.get("doctor_name"),
            interaction_type=data.get("interaction_type"),
            topics=data.get("topics"),
            sentiment=data.get("sentiment"),
            outcomes=data.get("outcomes"),
            follow_up=data.get("follow_up"),
        )

        db.add(new_interaction)
        db.commit()
        db.refresh(new_interaction)

        return {
            "input": input_text,
            "data": data
        }

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Error: {str(e)}"
        )

    finally:
        db.close()


# OPTIONAL (for demo bonus)
@app_api.get("/interactions")
def get_interactions():
    db = SessionLocal()
    data = db.query(Interaction).all()
    db.close()
    return data