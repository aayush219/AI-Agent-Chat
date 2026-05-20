from datetime import datetime
from langchain.agents import create_agent
from langchain_ollama import ChatOllama
import uuid

import gradio as gr 
from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3

def get_date():
    """ Get the current date"""
    return datetime.now().strftime("%Y-%m-%d")


conn = sqlite3.connect(database="chatbot_memory.db", check_same_thread = False)
checkpointer = SqliteSaver(conn)

llm = ChatOllama(model = "qwen2.5:3b")



system_prompt = """ You are a helpful assistant.
Answer all user's queries appropriately.
Use the get_date tool only if the user is asking about today's date.
"""

agent = create_agent(
    model = llm, 
    tools = [get_date], 
    system_prompt = system_prompt,
    checkpointer= checkpointer
    )


def chat(message, history, thread_id):
    config = {"configurable":{"thread_id": thread_id}}
    response = agent.invoke(
        {"messages":[{"role": "user", "content": message}]},
        config)
    last_response = response['messages'][-1].content
    return last_response

#print(response['messages'][-1].content)

with gr.Blocks() as demo:
    gr.Markdown("#AI Chatbot")
    thread_id = gr.State(value = lambda: str(uuid.uuid4()))
    gr.ChatInterface(fn=chat, additional_inputs= thread_id)

demo.launch()