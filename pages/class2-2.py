import streamlit as st
import random as r

st.title("這是標題")
st.write(
    "這是一個用 `st.write` 顯示的字串，可以處理多種格式，例如;數字、文字、Markdown、數據框等。"
)
st.write(
    """
    這是一個用`st.write`顯示的字串，可以處理Markdown語法。
    例如：
* **粗體文字**
* *斜體文字*
* [連結](https://www.example.com)
* 代碼塊
    ```python
    print("Hello World")
    ```
    """
)
# st.number_input()
# 可以讓用戶輸入數字，設定step=1可以讓用戶輸入整數，如果要輸入十分位則設定step=0.1
# min_value和max_value可以設定最小值0和最大值100
number = st.number_input("請輸入一個數字", min_value=0, max_value=100, step=1)
st.write(f"你輸入的數字是{number}")
# value可以設定預設值為0
st.write("---")
st.write("練習")
number = st.number_input("請輸入一個分數", min_value=0, max_value=100, step=1)
if number > 89:
    st.write(f"你成績很好，你的成績是A")
elif number > 79:
    st.write(f"你成績很好，你的成績是B")
elif number > 69:
    st.write(f"你成績很好，你的成績是C")
elif number > 59:
    st.write(f"你成績很好，你的成績是D")
else:
    st.write(f"你成績不好，你的成績是F")

st.write("---")
st.write("###按鈕練習")
# st.button()可以讓用戶點擊按鈕
# key可以設定按鈕的名稱
# 如果按鈕被點擊，st.button就會返回True
st.button("點擊我", key="button")
if st.button("點擊我", key="ballons"):
    st.balloons()
if st.button("點擊我", key="snow"):
    st.snow()
st.write("---")
st.write("隨機數字")
# random.randint(1, 100)可以產生一個1到100之間的隨機整數
st.write(f"random.randint(1, 100) = {r.randint(1, 100)}")
if st.button("按我一下", key="random"):
    st.write(f"random.randint(1, 100) = {r.randint(1, 100)}")

# 透過session_state可以在將變數暫時存在瀏覽器當中，直到使用者重新整理整個網頁
# 按下元件、或是與元件互動，都不會讓session_state當中的變數消失
if "ans" not in st.session_state:
    st.session_state.ans = r.randint(1, 100)

st.write(f"存在於session_state的隨機數字={st.session_state.ans}")
