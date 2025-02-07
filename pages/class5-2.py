import streamlit as st
from openai import OpenAI
import dotenv
import os

dotenv.load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("猜謎遊戲")

if "history" not in st.session_state:
    st.session_state.history = []

for message in st.session_state.history:
    if message["role"] != "developer":
        with st.chat_message(message["role"]):
            st.write(message["content"])

message = st.chat_input("請輸入文字")  # 聊天輸入框元件

if message:
    st.session_state.history.append({"role": "user", "content": message})
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "developer", "content": "你是小明，只能用中文回應後續"}]
        + st.session_state.history,
    )
    st.session_state.history.append(
        {"role": "assistant", "content": completion.choices[0].message.content}
    )
    st.rerun()
