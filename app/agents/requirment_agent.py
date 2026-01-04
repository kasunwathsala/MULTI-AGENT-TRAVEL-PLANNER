from langchain.agents import create_agent


from app.agents.promots import REQUIREMENTS_AGENT_SYSTEM_PROMPT
from app.agents.response_models import RequirementsAgentResponseModel
from app.agents.tools import search_flight_availability
from app.core.llm import model

llm = ChatOpenAI(model=settings.OPENAI_MODEL_NAME, api=settings.OPENAI_API_KEY)

agent = create_agent(
    model=llm,
    tools=[search_flight_availability],
    system_prompt=REQUIREMENTS_AGENT_SYSTEM_PROMPT,
    response_model=ToolStrategy(RequirementsAgentResponseModel),
)

if __name__ == "__main__":
    for chunk in agent.stream(
        input={"message": ["I want to go to seoul(ICN) from Tokyo(NRT).My dates are flexible."]},
        stream_mode="updates",
    ):
        print(chunk)
    