import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from src.config import instruction


load_dotenv()
GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY



def ask_bot(user_message,instruction):
    # user_message = "can you tell me about menu?"
    # messages = [{"role":"system","content":instruction},
    # {"role":"user","content":user_message}]


    # llm = ChatGoogleGenerativeAI(model="gemini-pro")
    model = ChatGoogleGenerativeAI(model="gemini-pro", convert_system_message_to_human=True)
    #response = llm.invoke(message)
    respones=model(
    [
        SystemMessage(content=instruction),
        HumanMessage(content=user_message),
    ]
)
    return respones.content

if __name__ == "__main__":
    user_message = "hi how are you?"
    respones=ask_bot(user_message)
    print(respones)
    # print("Welcome to the chat bot")
    # message=ask_bot("what is a meaning of large language models?")
    # print(message)


