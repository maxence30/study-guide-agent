import asyncio

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from agents.explainer_agent import explainer_agent
from tools.file_writer import save_markdown_file
from tools.validation import validate_required_sections

APP_NAME = "study-guide-agent"
USER_ID = "user"
SESSION_ID = "session"


async def main():

    session_service = InMemorySessionService()

    await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
    )

    runner = Runner(
        agent=explainer_agent,
        app_name=APP_NAME,
        session_service=session_service,
    )

    topic = input("Topic: ")

    content = types.Content(
        role="user",
        parts=[types.Part(text=topic)],
    )

    async for event in runner.run_async(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=content,
    ):
        if event.is_final_response():

            response = event.content.parts[0].text

            print(response)

            save_path = save_markdown_file(
                "output/study_guide.md",
                response,
            )

            print(f"\n✅ Saved to: {save_path}")

            validation = validate_required_sections(response)

            if validation["valid"]:
                print("✅ Validation passed")
            else:
                print("\n❌ Missing sections:")
                for section in validation["missing_sections"]:
                    print(f"- {section}")


if __name__ == "__main__":
    asyncio.run(main())