from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from dotenv import load_dotenv
import os

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME")

reviewer_agent = LlmAgent(
    name="reviewer_agent",
    model=LiteLlm(model=MODEL_NAME),
    description="Reviews study guides.",
    instruction="""
You are a reviewer agent.

Review the study guide.

Return ONLY these sections:

## Common Mistakes

## Review Comments

## Final Summary

Keep comments short and constructive.
Do not rewrite the guide.
"""
)