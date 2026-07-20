from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from dotenv import load_dotenv
import os

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME")

practice_designer_agent = LlmAgent(
    name="practice_designer_agent",
    model=LiteLlm(model=MODEL_NAME),
    description="Creates beginner practice exercises.",
    instruction="""
You are a practice designer.

The user will give you:
- a topic
- an explanation

Do NOT explain the topic again.

Return ONLY these sections:

## Practice Exercise

## Expected Input

## Expected Output

## Hints

Create a short exercise suitable for a beginner.
""",
)