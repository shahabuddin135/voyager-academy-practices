from agents.extensions.models.litellm_model import LitellmModel
from agents import Agent, Runner, tool,function_tool, OpenAIChatCompletionsModel
from openai import AsyncOpenAI
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()

qroq_client = AsyncOpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

groq_model = OpenAIChatCompletionsModel(
    model="openai/gpt-oss-120b",
    openai_client=qroq_client
)

@function_tool
def double_it(num:int)->int:
    '''This tool is responsible to double any given integer '''
    return num * 2


code_buddy = Agent(
    name="Code Buddy",
    instructions="You are a helpful Coding assistant who helps with problem solving in code and writing code.",
    model= groq_model,
    tools=[double_it]
    )


async def main():

    result = Runner.run_streamed(code_buddy, "What is 26454 doubled?")
    
    async for event in result.stream_events():
        if event.type == "run_item_stream_event":
            item = event.item
            if item.type == "tool_call_item":
                print(f"[Agent Activity] Calling tool: {item.raw_item.name} with args: {item.raw_item.arguments}")
            elif item.type == "tool_call_output_item":
                print(f"[Agent Activity] Tool returned: {item.output}")
            elif item.type == "message_output_item":
                print(f"\n[Final Response]\n{result.final_output}")

if __name__ == "__main__":
    asyncio.run(main())

