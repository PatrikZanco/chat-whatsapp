import os
from decouple import config
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from openai import OpenAI
from langchain_community.llms import OpenAI



llm = OpenAI(temperature=0, openai_api_key=config("OPENAI_API_KEY"))
tools = load_tools(["wikipedia"], llm=llm)
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

print(agent.run("What are the current trending topics related to chatbots?"))