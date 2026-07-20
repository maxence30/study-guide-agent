import asyncio

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from agents.explainer_agent import explainer_agent
from agents.practice_designer_agent import practice_designer_agent
from agents.reviewer_agent import reviewer_agent

from tools.file_writer import save_markdown_file
from tools.validation import validate_required_sections

APP_NAME = "study-guide-agent"
USER_ID = "user"
SESSION_ID = "session"


async def run_agent(agent, text):

    session_service = InMemorySessionService()

    await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
    )

    runner = Runner(
        agent=agent,
        app_name=APP_NAME,
        session_service=session_service,
    )

    content = types.Content(
        role="user",
        parts=[types.Part(text=text)],
    )

    response = ""

    async for event in runner.run_async(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=content,
    ):
        if event.is_final_response():
            response = event.content.parts[0].text

    return response


async def main():

    topic = input("Topic: ")

    print("\nRunning Explainer Agent...\n")

    explanation = await run_agent(
        explainer_agent,
        topic,
    )

    print("Running Practice Designer Agent...\n")

    practice = await run_agent(
        practice_designer_agent,
        f"""
Topic:

{topic}

Explanation:

{explanation}
""",
    )

    draft = explanation + "\n\n" + practice

    print("Running Reviewer Agent...\n")

    review = await run_agent(
        reviewer_agent,
        draft,
    )

    final_markdown = draft + "\n\n" + review

    validation = validate_required_sections(
        final_markdown
    )

    save_markdown_file(
        "output/study_guide.md",
        final_markdown,
    )

    print(final_markdown)

    print("\n---------------------------")

    if validation["valid"]:
        print("Validation passed")
    else:
        print("Missing sections:")

        for section in validation["missing_sections"]:
            print("-", section)

    print("\nSaved in output/study_guide.md")


if __name__ == "__main__":
    asyncio.run(main())