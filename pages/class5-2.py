import streamlit as st
from openai import OpenAI
import dotenv
import os
import menu

menu.menu()

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
        messages=[
            {
                "role": "developer",
                "content": """
                只能用繁體中文(#zh-TW)回應後續對話
                請跟使用者玩一場猜謎遊戲，你需要先描述題目，接下來依照使用者回應的猜測給予提示
                提示只能說[是]與[否]，不可以提供太多資訊
                以下為猜謎遊戲的題目(一開始要提供給玩家的資訊):
                題目你自己出
                以下為答案(不能提供給玩家的資訊直到玩家差不多猜到的時候再公布答案):
                答案你自己出
               """,
            }
        ]
        + st.session_state.history,
    )
    st.session_state.history.append(
        {"role": "assistant", "content": completion.choices[0].message.content}
    )
    st.rerun()
