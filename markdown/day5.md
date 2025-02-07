# Python 與 Streamlit 課程筆記

## 📊 成績登記系統

### 1️⃣ 資料結構設計
- **字典 (Dictionary)**：用來儲存學生的姓名作為 key，對應的 value 是該學生各科成績。
- **巢狀結構**：學生名稱 → 科目 → 成績列表（List）。

```python
# 成績登記系統
grade = {
    "小明": {"國文": [100, 100, 100], "數學": [100, 100, 100], "英文": [100, 100, 100]},
    "小美": {"國文": [96, 98, 97], "數學": [91, 90, 93], "英文": [100, 97, 100]},
    "大雄": {"國文": [0, 0, 0], "數學": [0, 0, 0], "英文": [0, 0, 0]},
}
```

### 2️⃣ 學生成績查詢與計算
- **查詢成績**：使用巢狀索引查詢特定學生、科目、次數的成績。

```python
# 小明的數學成績
print(grade["小明"]["數學"])  # [100, 100, 100]

# 小美的第一次英文成績
print(grade["小美"]["英文"][0])  # 100

# 大雄的第二次國文成績
print(grade["大雄"]["國文"][1])  # 0
```

### 3️⃣ 平均成績計算
- **單科平均**：加總後除以成績數量。
- **總平均成績**：將所有科目成績加總後，除以科目數量。

```python
# 每位同學的國文段考平均成績
for name, subject in grade.items():
    avg = sum(subject["國文"]) / len(subject["國文"])
    print(f"{name} 國文段考平均成績: {avg}")

# 每位同學的總平均成績
for name, subject in grade.items():
    total = 0
    for score in subject.values():
        total += sum(score)
    avg = total / len(subject)
    print(f"{name} 總平均成績: {avg}")
```

### 4️⃣ 各科目平均成績整理

```python
# 找出所有科目
subjects = grade["小明"].keys()

# 建立科目平均成績的字典
avg_grade = {subject: [] for subject in subjects}

# 收集所有學生的成績
for subject in subjects:
    for name, scores in grade.items():
        avg_grade[subject] += scores[subject]

# 計算各科目的平均成績
for subject, scores in avg_grade.items():
    avg = sum(scores) / len(scores)
    print(f"{subject} 的平均成績: {avg}")
```

---

## 🤖 OpenAI API 使用

### 1️⃣ 安裝與設定
- **dotenv**：管理 API 金鑰，避免硬編碼。

```bash
pip install openai python-dotenv
```

### 2️⃣ 程式碼範例

```python
from openai import OpenAI
import dotenv
import os

dotenv.load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "developer", "content": "你是小明，只能用中文回應後續"},
        {"role": "user", "content": "你好小明"},
    ],
)

print(completion.choices[0].message.content)
```

---

## 🚀 Streamlit 應用

### 1️⃣ 側邊選單 (Sidebar Menu)

```python
import streamlit as st

def menu():
    st.sidebar.page_link("main.py", label="首頁", icon="🏠")
    st.sidebar.write("---")
    st.sidebar.page_link("pages/handbook.py", label="學習筆記", icon="📚")
    st.sidebar.page_link("pages/class2-2.py", label="Streamlit 基礎", icon="🎯")
```

### 2️⃣ 猜謎遊戲設計
- **Session State**：記錄聊天歷史。
- **Chat Input**：用戶輸入區。

```python
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

message = st.chat_input("請輸入文字")

if message:
    st.session_state.history.append({"role": "user", "content": message})
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "developer", "content": "只能用繁體中文回應，進行猜謎遊戲。"}
        ] + st.session_state.history,
    )
    st.session_state.history.append(
        {"role": "assistant", "content": completion.choices[0].message.content}
    )
    st.rerun()
```

---

## 📌 重點回顧
1. 巢狀字典方便管理複雜資料。
2. OpenAI API 與 dotenv 的結合增強安全性。
3. Streamlit 提供簡單直覺的互動介面設計，適合快速開發。

