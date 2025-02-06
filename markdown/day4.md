# Python & Streamlit 課程筆記

## 1. Streamlit 基本欄位元件

### 1.1 兩欄佈局 (Columns)
```python
col1, col2 = st.columns(2)
col1.button("按鈕1", key="button1")
col2.button("按鈕2", key="button2")
```
- 使用 `st.columns(2)` 建立兩個欄位。
- `col1.button` 與 `col2.button` 分別在不同欄位建立按鈕。

### 1.2 調整欄位寬度比例
```python
col1, col2 = st.columns([1, 2])
col1.button("按鈕1", key="button3")
col2.button("按鈕2", key="button4")
```
- `st.columns([1, 2])` 以比例設定欄位寬度，col2 會是 col1 的兩倍寬。

### 1.3 三欄佈局
```python
col1, col2, col3 = st.columns([1, 2, 3])
col1.button("按鈕1", key="button5")
col2.button("按鈕2", key="button6")
col3.button("按鈕3", key="button7")
```
- 三欄佈局，欄位寬度依比例分配。

### 1.4 使用 with 語法在欄位中加入元件
```python
col1, col2 = st.columns([1, 2])

with col1:
    if st.button("按鈕1", key="button8"):
        st.balloons()
    st.write("這是col1")

with col2:
    if st.button("按鈕2", key="button9"):
        st.write("這是col2")
```
- `with` 語法可在指定欄位內放置多個元件。
- 按鈕觸發氣球動畫或顯示文字。

### 1.5 動態建立多欄佈局
```python
col_num = st.number_input("請輸入欄位數量：", min_value=1)
cols = st.columns(col_num)

for i in range(len(cols)):
    with cols[i]:
        st.button(f"按鈕{i+1}", key=f"button{i+10}")
```
- `st.number_input` 讓使用者輸入欄位數量。
- 使用迴圈動態生成按鈕。

---

## 2. 點餐機應用
```python
if "cart" not in st.session_state:
    st.session_state.cart = []

col1, col2 = st.columns(2)
with col1:
    foodInput = st.text_input("請輸入食物")

with col2:
    if st.button("加入", key="add"):
        st.session_state.cart.append(foodInput)

st.write("### 購物車")
for index in range(len(st.session_state.cart)):
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"{st.session_state.cart[index]}")
    with col2:
        if st.button("刪除", key=f"remove{index+1}"):
            st.session_state.cart.pop(index)
            st.rerun()
```
- 使用 `st.session_state` 儲存購物車資料。
- 動態顯示購物車內容與刪除功能。

---

## 3. Python 基本語法

### 3.1 算術指定運算子
```python
a = 1
a += 1  # a = a + 1
a -= 1  # a = a - 1
a *= 2  # a = a * 2
a /= 2  # a = a / 2
a //= 2 # a = a // 2
a %= 2  # a = a % 2
a **= 2 # a = a ** 2
```

### 3.2 運算子優先順序
1. `()` 括號
2. `**` 次方
3. `+` `-` 加減
4. `*` `/` `//` `整數除法`
5. `==` `!=` `>` `<` `>=` `<=` 比較運算子
6. `and` `or` 邏輯運算子
7. `=` `+=` `-=` `*=` `/=` `//=` `%=` `**=` 指定運算子

---

## 4. 迴圈控制

### 4.1 while 迴圈
```python
i = 0
while i < 5:
    print(i)
    i += 1
```
- 條件為 `True` 時執行，否則跳出迴圈。

### 4.2 break 跳出迴圈
```python
i = 0
while i < 5:
    print(i)
    for j in range(5):
        print(j)
        if j == 3:
            break
    i += 1
```
- `break` 直接跳出當前迴圈。

---

## 5. 字典 (Dictionary)

### 5.1 基本操作
```python
d = {"a": 1, "b": 2, "c": 3}

# 取得 key 和 value
print(d.keys())
print(d.values())

# 新增與修改
d["d"] = 4

# 檢查 key 是否存在
print("a" in d)

# 刪除 key
print(d.pop("a"))
```

### 5.2 巢狀字典
```python
d = {"a": [1, 2, {"e": 40, "f": 50}], "b": {"c": 4, "d": 5}}
print(d["a"][2]["f"])  # 50
```

