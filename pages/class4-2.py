import streamlit as st

st.title("點餐機")

if "cart" not in st.session_state:
    st.session_state.cart = []


col1, col2 = st.columns(2)
with col1:
    foodInput = st.text_input("請輸入食物")

with col2:
    if st.button("加入", key="add"):  # 如果按下加入按鈕，就會加入購物車
        st.session_state.cart.append(foodInput)

st.write("### 購物車")
for index in range(len(st.session_state.cart)):
    col1, col2 = st.columns(2)  # 建立2個欄位
    with col1:
        st.write(f"{st.session_state.cart[index]}")  # 顯示購物車中的食物

    with col2:
        if st.button("刪除", key=f"remove{index+1}"):  # 如果按鈕被按下
            st.session_state.cart.pop(index)  # 將購物車中的食物刪除
            st.rerun()  # 刷新網頁
