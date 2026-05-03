import os
from dotenv import load_dotenv
from typing import TypedDict

from langchain_groq import ChatGroq
from langgraph.graph import StateGraph

from tools import log_interaction

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model="gemma2-9b-it"
)


class AgentState(TypedDict):
    input: str
    output: dict


def agent_node(state: AgentState):
    # For now using tool directly
    result = log_interaction.invoke(state["input"])
    return {"output": result}


graph = StateGraph(AgentState)
graph.add_node("agent", agent_node)
graph.set_entry_point("agent")

app = graph.compile()