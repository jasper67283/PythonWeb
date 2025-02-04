import streamlit as st

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
