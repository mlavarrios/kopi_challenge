from google import genai

from src.kopi.infrastructure.entities import LLMAnswer
from src.settings import Settings

settings = Settings.get_settings()

class AIRepository:
    def __init__(self, settings: Settings):
        self.client = genai.Client(api_key=settings.gemini_api_key)

    async def generate_response(self, prompt: str) -> LLMAnswer:
        response = self.client.models.generate_content(
            model='gemini-2.0-flash-001', contents=prompt
        )
        print(response.text)

        return LLMAnswer(text=response.text) if hasattr(response, 'text') else LLMAnswer(text="No response")
