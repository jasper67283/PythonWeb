# Python 與 Streamlit 筆記

## 字串格式化

```python
name = "apple"
age = 18
print(f"Hello, my name is {name}, I am {age} years old")  # f-string
```

- f-string 可以將變數或其他型態的資料放到字串中的 `{}`，方便插入變數值。

## 字串長度與型態判斷

```python
print(len("apple"))  # len() 可計算字串長度
print(len("，"))
```

```python
print(type(1))  # <class 'int'>
print(type("apple"))  # <class 'str'>
print(type(1.0))  # <class 'float'>
print(type(True))  # <class 'bool'>
```

- `len()` 用於取得字串長度。
- `type()` 可查看變數型態。

## 型態轉換

```python
print(int(1.0))
print(float("1"))
print(str(1))
print(str(1.234))
print(bool(1))
print(bool("1"))
print(bool(1.234))
print(float("1.234"))
```

- 可透過 `int()`、`float()`、`str()`、`bool()` 進行型態轉換。
- 不能將非數字字串轉換為數字，否則會報錯。

## 使用者輸入與條件判斷

```python
a = input("請輸入一些文字:")
print(int(a) * int(a))
print(type(a))  # input() 讀入的資料預設為字串
```

### 密碼檢查

```python
password = input("請輸入密碼:")
if password == "1234":
    print("歡迎使用Python")
elif password == "5678":
    print("歡迎使用VSCode")
elif password == "9012":
    print("歡迎使用Discord")
else:
    print("密碼錯誤")
```

- `if-elif-else` 可用來處理多個條件判斷。

## 比較與邏輯運算子

```python
print(1 == 1)  # True
print(1 != 1)  # False
print(1 > 1)   # False
print(1 >= 1)  # True
```

```python
print(True and True)
print(True or False)
print(not True)
```

- `and`：兩者皆為 `True` 才為 `True`
- `or`：其中之一為 `True` 即為 `True`
- `not`：取反

## 運算優先順序

1. `()` 括號
2. `**` 次方
3. `+ -` 加減
4. `* / //` 乘除
5. `== != > < >= <=` 比較運算子
6. `and or` 邏輯運算子

---

# Streamlit 應用

## 顯示文字與標題

```python
import streamlit as st
st.title("這是標題")
st.write("這是一個用 `st.write` 顯示的字串，可以處理多種格式，例如數字、文字、Markdown。")
```

## Markdown 顯示

```python
st.write(
    """
    * **粗體文字**
    * *斜體文字*
    * [連結](https://www.example.com)
    * 代碼塊:
    ```python
    print("Hello World")
    ```
    """
)
```

## 數字輸入

```python
number = st.number_input("請輸入一個數字", min_value=0, max_value=100, step=1)
st.write(f"你輸入的數字是 {number}")
```

## 成績判斷

```python
number = st.number_input("請輸入一個分數", min_value=0, max_value=100, step=1)
if number > 89:
    st.write("你成績很好，你的成績是A")
elif number > 79:
    st.write("你的成績是B")
elif number > 69:
    st.write("你的成績是C")
elif number > 59:
    st.write("你的成績是D")
else:
    st.write("你的成績是F")
```

## 按鈕互動

```python
if st.button("點擊我"):
    st.balloons()
if st.button("下雪效果"):
    st.snow()
```

## 生成隨機數字

```python
import random as r
st.write(f"隨機數字: {r.randint(1, 100)}")
```

## 使用 `session_state`

```python
if "ans" not in st.session_state:
    st.session_state.ans = r.randint(1, 100)
st.write(f"存於 session_state 的隨機數字 = {st.session_state.ans}")
```

## 猜數字遊戲

```python
st.title("猜數字遊戲")
if "ans" not in st.session_state:
    st.session_state.ans = r.randint(1, 100)
guess = st.number_input("請輸入一個數字：", step=1, min_value=1, max_value=100)
if guess == st.session_state.ans:
    st.write("恭喜你猜對了！")
    st.balloons()
elif guess > st.session_state.ans:
    st.write("數字太大了！")
else:
    st.write("數字太小了！")
```

- `session_state` 用於存儲變數，即使頁面重新渲染，變數仍然存在。
