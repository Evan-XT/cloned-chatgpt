from langchain.chains.conversation.base import ConversationChain
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferWindowMemory

def chat_robot(prompt,given_memory):
    set_model=ChatOpenAI(model="deepseek-chat",api_key="sk-ceaa047654f3462d93e37474dbae11af",
                     base_url="https://api.deepseek.com")
    
    given_memory.save_context({"input":"你好,我是Evan"},{"output":"您好，Evan"})
    given_memory.save_context({"input":"注意，不要提及我们之前的对话"},{"output":"好的"})
    given_memory.load_memory_variables({})
    chain=ConversationChain(llm=set_model,memory=given_memory)
    response=chain.invoke({"input":prompt})
    return response["response"]

