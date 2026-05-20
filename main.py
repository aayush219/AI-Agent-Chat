from datetime import datetime
from langchain.agents import create_agent
from langchain_ollama import ChatOllama

import gradio as gr 


def get_date():
    """ Get the current date"""
    return datetime.now().strftime("%Y-%m-%d")



llm = ChatOllama(model = "qwen2.5:3b")

system_prompt = """ You are a helpful assistant.
Answer all user's queries.
Use the get_date tool if the user is asking about today's date.
"""

agent = create_agent(model = llm, tools = [get_date], system_prompt = system_prompt)


def chat(message, history):
    response = agent.invoke({"messages":[{"role": "user", "content": message}]})
    last_response = response['messages'][-1].content
    return last_response

#print(response['messages'][-1].content)

with gr.Blocks() as demo:
    gr.Markdown("#AI Chatbot")
    gr.ChatInterface(fn=chat)

demo.launch()