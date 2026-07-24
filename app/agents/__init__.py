if __package__:
    from .travel_system_agents import (
        requirments_agent,
        planner_agent,
        booker_agent,
    )
else:
    # Allow running this file directly: python app/agents/__init__.py
    import os
    import sys

    _project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    if _project_root not in sys.path:
        sys.path.insert(0, _project_root)

    from app.agents.travel_system_agents import (
        requirments_agent,
        planner_agent,
        booker_agent,
    )

__all__ = ["requirments_agent", "planner_agent", "booker_agent"]
