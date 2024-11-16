from typing import Any, Dict, List, Optional
#import autogpt
#from autogpt.core.resource.model_providers import LanguageModelProvider
#from autogpt.core.planning.base import Task
#from autogpt.core.plugin.base import Block
from jina import Client

class JinaSearchBlock(Block):
    def __init__(self, api_key: str):
        self.client = Client(api_key=api_key)

    async def run(self, task: Task, dependencies: Dict[str, Any]) -> Any:
        query = task.input
        try:
            response = self.client.search(query)
            return {"results": response.matches}
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def description() -> str:
        return "Searches the web using Jina.ai API"

    @staticmethod
    def required_dependencies() -> List[str]:
        return []

