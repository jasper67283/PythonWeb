import streamlit as st

st.title("數字金字塔")
number = st.number_input("請輸入一個數字(1~9)", min_value=1, max_value=9, step=1)
st.write("數字金字塔")
for i in range(1, number + 1):
    st.write(f"{i} " * i)

st.write("---")
st.write("文字輸入元件")
# st.text_input指令格式 st.text_input(輸入欄位的標題, value="預設顯示的文字")
test = st.text_input("請輸入一個文字", value="預設顯示的文字")
st.write(f"你輸入的文字是 {test}")
