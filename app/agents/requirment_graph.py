import json
from typing import Optional

from langchain.messages import HumanMessage, AIMessage
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.types import interrupt, Command
from langgraph.checkpoint.memory import InMemorySaver

from app.agents.travel_system_agents import requirements_agent


checkpointer = InMemorySaver()


class RequirementsGraphState(MessagesState):
    requirements_complete: bool
    interruption_message: str
    requirements: Optional[dict]