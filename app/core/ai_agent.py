from app.config.settings import settings
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch
from langgraph.prebuilt import create_react_agent 
from langchain_core.messages import AIMessage, HumanMessage
from langsmith import traceable
import os

@traceable
def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt):

    llm = ChatGroq(model=llm_id)
    tools = [TavilySearch(max_results=2)] if allow_search else []
    agent = create_react_agent(
        model=llm,
        tools=tools,
        prompt=system_prompt
    )

    state = {"messages": [HumanMessage(content=msg) for msg in query]}
    response = agent.invoke(state)
    messages = response.get("messages")
    ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]

    return ai_messages[-1]