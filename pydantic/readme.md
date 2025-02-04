[PydanticAI Agents](https://ai.pydantic.dev/)
 - support sync, async, stream
 - restrict usage (tokens), retry count on tools
 - support for type checking (input/output)

Multiple ways to use functions as tools :

- @agent.tool
- @agent.tool_plain (for when we don't need Agent Context passed to function)
- via tools parameter: ``` agent_b = Agent(
    'google-gla:gemini-1.5-flash',
    deps_type=str,
    tools=[  
        Tool(roll_die, takes_ctx=False),
        Tool(get_player_name, takes_ctx=True),
    ],
)```

Dynamic function tools- Can modify usage/other attributes of a tool via "prepare"[see ToolPrepareFunc]. See https://ai.pydantic.dev/tools/#function-tools-and-schema

Instrumentation support via Pydantic Logfire

More complex graph based workflows/ delegation possible.
