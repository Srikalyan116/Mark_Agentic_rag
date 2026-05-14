from dataclasses import dataclass
from typing import Callable, Dict, Any


@dataclass
class Tool:
    name: str
    description: str
    function: Callable[[str], str]


class ToolRegistry:
    def __init__(self):
        self.tools: Dict[str, Tool] = {}

    def register(self, tool: Tool) -> None:
        self.tools[tool.name] = tool

    def run(self, name: str, argument: str) -> str:
        if name not in self.tools:
            raise ValueError(f"Tool not found: {name}")
        return self.tools[name].function(argument)

    def describe(self) -> list[dict[str, Any]]:
        return [
            {"name": tool.name, "description": tool.description}
            for tool in self.tools.values()
        ]
