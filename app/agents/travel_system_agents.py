from langchain.agents import create_agent


from app.agents.prompts import REQUIREMENTS_AGENT_SYSTEM_PROMPT, PLANNER_AGENT_SYSTEM_PROMPT, BOOKER_AGENT_SYSTEM_PROMPT
from app.agents.response_models import RequirementsAgentResponseModel, PlannerAgentResponseModel, BookerAgentResponseModel
from app.agents.tools.flight_tools import search_flight_availability
from app.agents.tools.planner_tools import web_search
from app.agents.tools.booker_tools import book_flight, book_hotel, search_hotels
from langchain.agents.structured_output import ToolStrategy

from app.core.llm import llm 



requirments_agent = create_agent(
    model=llm,
    tools=[search_flight_availability],
    system_prompt=REQUIREMENTS_AGENT_SYSTEM_PROMPT,
    response_format=ToolStrategy(RequirementsAgentResponseModel),
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
    for chunk in requirments_agent.stream(
        input={"message": ["I want to go to seoul(ICN) from Tokyo(NRT).My dates are flexible."]},
        stream_mode="updates",
    ):
        print(chunk)
    