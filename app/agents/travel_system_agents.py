from langchain.agents import create_agent


from app.agents.promopts import REQUIREMENTS_AGENT_SYSTEM_PROMPT
from app.agents.response_models import RequirementsAgentResponseModel
from app.agents.tools import search_flight_availability
from app.core.llm import model



requirments_agent = create_agent(
    model=llm,
    tools=[search_flight_availability],
    system_prompt=REQUIREMENTS_AGENT_SYSTEM_PROMPT,
    response_model=ToolStrategy(RequirementsAgentResponseModel),
)

planner_agent = create_agent(
    model=llm,
    name="planner",
    tools=[web_search],
    response_format=ToolStrategy(PlannerAgentResponseModel),
    system_prompt=PLANNER_AGENT_SYSTEM_PROMPT,
)

booker_agent = create_agent(
    model=llm,
    name="booker",
    tools=[book_flight, book_hotel, search_hotels],
    response_format=ToolStrategy(BookerAgentResponseModel),
    system_prompt=BOOKER_AGENT_SYSTEM_PROMPT,
)

if __name__ == "__main__":
    for chunk in agent.stream(
        input={"message": ["I want to go to seoul(ICN) from Tokyo(NRT).My dates are flexible."]},
        stream_mode="updates",
    ):
        print(chunk)
    