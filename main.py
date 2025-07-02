import streamlit as st
from utils import chat_robot
from langchain.memory import ConversationBufferWindowMemory


st.title("ChatGPT(4o)")

if "memory" not in st.session_state:
    st.session_state["memory"]=ConversationBufferWindowMemory(return_messages=True)
    st.session_state["messages"]=[{"role":"ai","content":"你好，我是OpenAI 最新的推理模型ChatGPT（4o），请问有什么可以帮您?"}]

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

prompt=st.chat_input()
if prompt:    
    st.session_state["messages"].append({"role":"human","content":prompt})
    st.chat_message("human").write(prompt)
    with st.spinner("AI正在思考"):
        response = chat_robot(prompt = prompt,given_memory = st.session_state["memory"])
        st.session_state["messages"].append({"role":"ai","content":response})
        st.chat_message("ai").write(response)
    

