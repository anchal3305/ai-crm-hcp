from langchain.tools import tool
from langchain_groq import ChatGroq
import os
import json
from dotenv import load_dotenv

load_dotenv()

# Initialize LLM
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.3-70b-versatile"
)


# 🔧 Helper function to clean LLM output
def clean_json_output(content: str):
    content = content.strip()

    # Remove markdown ```json ``` if present
    if content.startswith("```"):
        content = content.replace("```json", "").replace("```", "").strip()

    try:
        return json.loads(content)
    except:
        return {
            "error": "JSON parsing failed",
            "cleaned_output": content
        }


@tool
def log_interaction(text: str):
    """Extract structured interaction data from user input using LLM."""

    try:
        prompt = f"""
        Extract structured CRM interaction details from the text below.

        Return ONLY valid JSON in this format:

        {{
            "doctor_name": "",
            "interaction_type": "Meeting or Call",
            "topics": "",
            "sentiment": "Positive/Neutral/Negative",
            "outcomes": "",
            "follow_up": ""
        }}

        Text: {text}
        """

        response = llm.invoke(prompt)

        return clean_json_output(response.content)

    except Exception as e:
        return {
            "error": "LLM call failed",
            "details": str(e)
        }


@tool
def edit_interaction(data: dict):
    """Edit an existing interaction record."""

    return {
        "status": "updated",
        "updated_data": data
    }


@tool
def get_hcp_details(name: str):
    """Fetch details of a healthcare professional."""

    return {
        "doctor_name": name,
        "specialization": "Cardiology",
        "hospital": "Apollo Hospital"
    }


@tool
def suggest_followup(text: str):
    """Suggest follow-up actions based on interaction using LLM."""

    try:
        prompt = f"""
        Based on the interaction below, suggest a clear next follow-up step.

        Text: {text}
        """

        response = llm.invoke(prompt)

        return {
            "suggestion": response.content.strip()
        }

    except Exception as e:
        return {
            "error": "Follow-up generation failed",
            "details": str(e)
        }


@tool
def analyze_sentiment(text: str):
    """Analyze sentiment of the interaction using LLM."""

    try:
        prompt = f"""
        Classify the sentiment as:
        Positive, Neutral, or Negative.

        Text: {text}
        """

        response = llm.invoke(prompt)

        return {
            "sentiment": response.content.strip()
        }

    except Exception as e:
        return {
            "error": "Sentiment analysis failed",
            "details": str(e)
        }