import streamlit as st

with st.expander("Day1"):
    st.code(
        """
        # 這是註解,不會被執行
        # CTRL+? 可以把框選的範圍做 快速註解/取消註解

        print("Hello World")  # print是在終端機顯示文字的指令
        # 基本型態
        print(1)  # int
        print(1.0)  # float
        print(1.234)  # float
        print("apple")  # str
        print(True)  # bool
        print(False)  # bool

        print(1 + 1)  # 2
        print("1" + "1")  # 11，字串加法是字串拼接

        # 變數
        a = 10  # 新增一個儲存空間並取名為a
        # "="的功能是將右邊的值存入左邊的變數
        print(a)  # 在終端機顯示a的值
        a = "apple"  # 將a的值變成"apple"
        print(a)  # 在終端機顯示a的值
        print(1 + 1)  # 加法後的值
        print(1 - 1)  # 減法後的值
        print(1 * 1)  # 乘法後的值
        print(1 / 1)  # 除法後的值
        print(1 // 1)  # 整數除法後的值
        print(1**1)  # 次方後的值
        print(1 % 1)  # 取餘數後的值
        # 優先順序
        # 1. ( ) 誇號
        # 2. 乘除次方
        # 3. 加減
        # 4. 比較
        # 5. 邏輯
        # 6. 位元運算

        # 字串
        s = "apple"  # 字串
        s = "apple"  # 重複宣告
        s = "apple"  # 重複宣告
    """
    )

with st.expander("Day2"):
    st.write(
        '''
### Python 課程筆記

---

## **字串格式化**
- `f-string` 用 `{}` 來嵌入變數或表達式：
  ```python
  name = "apple"
  age = 18
  print(f"Hello, my name is {name}, I am {age} years old")
  ```
- `len()` 取得字串長度：
  ```python
  print(len("apple"))  # 5
  print(len("，"))  # 1
  ```
- `type()` 取得變數型態：
  ```python
  print(type(1))  # <class 'int'>
  print(type("apple"))  # <class 'str'>
  print(type(1.0))  # <class 'float'>
  print(type(True))  # <class 'bool'>
  ```

---

## **型態轉換**
- 轉換變數型態：
  ```python
  print(int(1.0))  # 1
  print(float("1"))  # 1.0
  print(str(1))  # "1"
  print(bool(1))  # True
  print(float("1.234"))  # 1.234
  ```
- **錯誤示範**：
  ```python
  print(int("hello"))  # 會報錯
  ```

---

## **使用 `input()` 讀取輸入**
- `input()` 會回傳 **字串型態**：
  ```python
  a = input("請輸入一些文字:")
  print(type(a))  # <class 'str'>
  ```
- 轉換為 `int`：
  ```python
  a = int(a)
  print(type(a))  # <class 'int'>
  ```

---

## **比較運算子**
| 運算子 | 說明 |
|--------|------|
| `==`  | 相等 |
| `!=`  | 不等於 |
| `>`   | 大於 |
| `<`   | 小於 |
| `>=`  | 大於等於 |
| `<=`  | 小於等於 |

```python
print(1 == 1)  # True
print(1 != 1)  # False
print(1 > 1)   # False
print(1 < 1)   # False
print(1 >= 1)  # True
print(1 <= 1)  # True
```

---

## **邏輯運算子**
| 運算子 | 說明 |
|--------|------|
| `and` | 兩個條件都要成立 |
| `or`  | 只要一個條件成立 |
| `not` | 反向判斷 |

```python
print(True and True)  # True
print(True and False)  # False
print(False or True)  # True
print(not True)  # False
```

---

## **運算優先順序**
1. `()` 括號
2. `**` 次方
3. `+ -` 加減
4. `* / //` 乘除
5. `== != > < >= <=` 比較
6. `and or` 邏輯運算子

---

## **密碼驗證**
- 使用 `if-elif-else` 來判斷密碼：
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

---

## **Streamlit 基本應用**
### **標題與文字**
- `st.title()` 設定標題
- `st.write()` 顯示文字與 Markdown
  ```python
  import streamlit as st
  st.title("這是標題")
  st.write("這是一個顯示的字串")
  ```
- Markdown 支援：
  ```python
  st.write("""
  * **粗體**
  * *斜體*
  * [連結](https://www.example.com)
  * 代碼塊：
  ```python
  print("Hello World")
  ```
  """")
  ```

---

## **數字輸入**
- `st.number_input()` 讓用戶輸入數字：
  ```python
  number = st.number_input("請輸入一個數字", min_value=0, max_value=100, step=1)
  st.write(f"你輸入的數字是 {number}")
  ```

### **成績判斷**
```python
number = st.number_input("請輸入一個分數", min_value=0, max_value=100, step=1)
if number > 89:
    st.write("你的成績是 A")
elif number > 79:
    st.write("你的成績是 B")
elif number > 69:
    st.write("你的成績是 C")
elif number > 59:
    st.write("你的成績是 D")
else:
    st.write("你的成績是 F")
```

---

## **按鈕與動畫**
- `st.button()` 讓用戶點擊：
  ```python
  if st.button("點擊我"):
      st.balloons()
  ```

---

## **隨機數**
- `random.randint(a, b)` 生成範圍內隨機數：
  ```python
  import random as r
  st.write(f"隨機數字: {r.randint(1, 100)}")
  ```

- **Session State 記住變數**
  ```python
  if "ans" not in st.session_state:
      st.session_state.ans = r.randint(1, 100)

  st.write(f"存在於 session_state 的隨機數字: {st.session_state.ans}")
  ```

---

## **猜數字遊戲**
```python
import streamlit as st
import random as r

st.title("猜數字遊戲")

if "ans" not in st.session_state:
    st.session_state.ans = r.randint(1, 100)

guess = st.number_input("請輸入一個數字：", step=1, min_value=1, max_value=100)

if guess == st.session_state.ans:
    st.write("恭喜你猜對了！")
    st.balloons()
elif guess > st.session_state.ans:
    st.write("猜錯了！數字太大了！")
else:
    st.write("猜錯了！數字太小了！")
```
'''
    )
