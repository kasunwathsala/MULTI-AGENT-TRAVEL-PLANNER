from langchain.agents import create_agent
from lagnchain_openai import ChatOpenAI

from app.agents.promots import REQUIREMENTS_AGENT_SYSTEM_PROMPT
from app.agents.response_models import RequirementsAgentResponseModel
from app.agents.tools import search_flight_availability

llm = ChatOpenAI(model=settings.OPENAI_MODEL_NAME, api=settings.OPENAI_API_KEY)

agent = create_agent(
    model=llm,
    tools=[search_flight_availability],
    system_prompt=REQUIREMENTS_AGENT_SYSTEM_PROMPT,
    response_model=RequirementsAgentResponseModel,
)