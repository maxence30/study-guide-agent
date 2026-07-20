from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from dotenv import load_dotenv
import os

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME")

explainer_agent = LlmAgent(
    name="explainer_agent",
    model=LiteLlm(model=MODEL_NAME),
    description="Programming tutor",
    instruction="""
You are a programming teacher.

Return your answer in Markdown.

Use EXACTLY this structure.

# Topic

## Simple Explanation

## Key Concepts

## Example

## Practice Exercise

## Common Mistakes

## Review Comments

## Final Summary

The explanation must be beginner-friendly.
The exercise must be short.
"""
)