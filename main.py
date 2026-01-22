from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI 
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_tavily import TavilySearch
from typing import List
from pydantic import BaseModel, Field
# from tavily import TavilyClient
load_dotenv()

class Source(BaseModel):
    """A source for the information retrieved by the agent."""
    url: str = Field(description="The URL of the source")

class AgentResponse(BaseModel):
    """The response from the agent."""
    answer: str = Field(description="The answer to the user's question")
    sources: List[Source] = Field(default_factory=list, description="The sources for the information")    

# tavily = TavilyClient()

# @tool
# def search_web(query: str) -> str:
#     """
#     Tool that searches the web for a given query.
#     Args:
#         query: The search query.
#     Returns:
#         The search results.
#     """
#     print(f"Searching the web for: {query}")
#     # return "Web search results for " + query
#     return tavily.search(query=query)

llm = ChatOpenAI()
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)

def main():
    print("Hello from langchain-course!")
    response = agent.invoke({"messages":HumanMessage(content="What is the capital of France?")})
    print("Agent response:", response)



if __name__ == "__main__":
    main()
