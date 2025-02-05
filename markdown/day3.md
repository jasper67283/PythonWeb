# Python 課程筆記

## for 迴圈
- `for` 會搭配 `in` 來使用，`in` 後面接一個有範圍的物件。
- `range(5)` 產生 `0` 到 `4` 的數字，不包含 `5`，如果要包含 `5` 則使用 `range(6)`。
- `i` 是迴圈變數，每回合會從範圍中取一個資料出來。

```python
for i in range(5):
    print(i)
```

### 設定起始值與結束值
```python
for i in range(1, 5):
    print(i)  # 1, 2, 3, 4
```

### 設定起始值、結束值與間隔值
```python
for i in range(1, 10, 2):
    print(i)  # 1, 3, 5, 7, 9
```

## `random.randrange()` 函數
- `random.randrange(start, stop, step)` 產生一個指定範圍內的隨機數。

```python
import random
for i in range(1, 10):
    print(random.randrange(1, 10))
```

## List (列表)
### 創建列表
```python
print([])  # 空的列表
print([1, 2, 3])  # 含有 3 個元素的列表
print([1, 2, 3, "a", "b", "c"])  # 含有 6 個元素的列表
print([1, True, "a", 1.23])  # 含有不同類型的元素
```

### 讀取元素
```python
L = [1, 2, 3, "a", "b", "c"]
print(L[0])  # 1
print(L[3])  # "a"
print(len(L))  # 6
```

### 走訪元素
```python
for i in range(len(L)):
    print(L[i])

for i in range(0, len(L), 2):
    print(L[i])  # 1, 3, "b"

for i in L:
    print(i)  # 1, 2, 3, "a", "b", "c"
```

### 切片操作
```python
R = [1, 2, 3, "a", "b", "c"]
print(R[::2])  # [1, 3, "b"]
print(R[1:4])  # [2, 3, "a"]
print(R[1:4:2])  # [2, "a"]
```

### 修改元素
```python
R[0] = 2
print(R)  # [2, 2, 3, "a", "b", "c"]
```

## Call by Value vs Call by Reference
```python
a = 1
b = a
b = 2
print(a, b)  # 1, 2
```

```python
a = [1, 2, 3]
b = a  # 共享記憶體位置
b[0] = 2
print(a, b)  # [2, 2, 3], [2, 2, 3]
```

```python
a = [1, 2, 3]
b = a.copy()  # 複製列表
b[0] = 2
print(a, b)  # [1, 2, 3], [2, 2, 3]
```

## List 操作
### `append()`
```python
L = [1, 2, 3]
L.append(4)
print(L)  # [1, 2, 3, 4]
```

### 移除元素
```python
L = ["a", "b", "c", "d", "a"]
L.remove("a")  # 移除第一個 'a'
```

```python
L.pop(0)  # 移除 index 0 的元素
L.pop()  # 移除最後一個元素
print(L)
```

## Streamlit 基礎應用
### 數字金字塔
```python
import streamlit as st

st.title("數字金字塔")
number = st.number_input("請輸入一個數字(1~9)", min_value=1, max_value=9, step=1)
st.write("數字金字塔")
for i in range(1, number + 1):
    st.write(f"{i} " * i)
```

### 文字輸入元件
```python
st.write("---")
st.write("文字輸入元件")
test = st.text_input("請輸入一個文字", value="預設顯示的文字")
st.write(f"你輸入的文字是 {test}")
```

### Markdown 檔案讀取
```python
import streamlit as st
import os

hd_book_files = os.listdir("markdown")
for file_name in hd_book_files:
    with st.expander(file_name[:-3]):
        with open(f"markdown/{file_name}", "r", encoding="utf-8") as file:
            test = file.read()
            st.markdown(test)
```

