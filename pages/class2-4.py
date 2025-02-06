import streamlit as st
import random as r

st.title("猜數字遊戲")

if "ans" not in st.session_state:
    st.session_state.ans = r.randint(1, 100)

if "min_value" not in st.session_state:
    st.session_state.min_value = 1

if "max_value" not in st.session_state:
    st.session_state.max_value = 100

guess = st.number_input("請輸入一個數字：", step=1, min_value=1, max_value=100)

if guess == st.session_state.ans:
    st.write("恭喜你猜對了！")
    st.balloons()
elif guess > st.session_state.ans:
    st.write("猜錯了！數字太大了！")
    if guess < st.session_state.max_value:
        st.session_state.max_value = guess
else:
    st.write("猜錯了！數字太小了！")
    if guess > st.session_state.min_value:
        st.session_state.min_value = guess

st.write(f"數字範圍:{st.session_state.min_value} ~ {st.session_state.max_value}")
