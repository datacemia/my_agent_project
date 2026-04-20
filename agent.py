from agents import Agent
from tools import word_counter

my_agent = Agent(
    name="Assistant with tools",
    instructions="You are helpful. Use the word_counter tool when needed.",
    tools=[word_counter]
)