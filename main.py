from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI 
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_tavily import TavilySearch
# from tavily import TavilyClient
load_dotenv()

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
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from langchain-course!")
    response = agent.invoke({"messages":HumanMessage(content="What is the capital of France?")})
    print("Agent response:", response)



if __name__ == "__main__":
    main()
