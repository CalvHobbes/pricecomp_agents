## Price Comparison using HF smolagents

- Relatively easy to make a standard pythni function a tool - add @tool and describe the function
- Single agent - use CodeAgent and supply tool
- Multi agent - create ManagedAgent and supply tools and then provide each ManagedAgent to the "manager" agent - e.g. CodeAgent
- Can use GradioUI out of the box
  ```
  from smolagents import GradioUI
  GradioUI(agent).launch()
  ```
