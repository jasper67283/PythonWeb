# 成績登記系統，key是學生名字，value是成績，每個科目有3個成績
grade = {
    "小明": {"國文": [100, 100, 100], "數學": [100, 100, 100], "英文": [100, 100, 100]},
    "小美": {"國文": [96, 98, 97], "數學": [91, 90, 93], "英文": [100, 97, 100]},
    "大雄": {"國文": [0, 0, 0], "數學": [0, 0, 0], "英文": [0, 0, 0]},
}

# 取的小明的數學成績
print(grade["小明"]["數學"])  # [100, 100, 100]
# 取得小美的第一次英文成績
print(grade["小美"]["英文"][0])  # 100
# 取得大雄的第二次國文成績
print(grade["大雄"]["國文"][1])  # 0
# 印出每一位同學國文段考平均成績
for name, subject in grade.items():
    avg = sum(subject["國文"]) / len(subject["國文"])
    print(f"{name} 國文段考平均成績: {avg}")
# 印出每一位同學總平均成績
for name, subject in grade.items():
    total = 0
    for score in subject.values():
        total += sum(score)
    avg = total / len(subject)
    print(f"{name} 總平均成績: {avg}")

# 整理全校各科目的平均成績
# 1. 先找出所有的科目列表
subjects = grade["小明"].keys()
print(subjects)  # ['國文', '數學', '英文']

# 2. 建立一個dict用來存放各科目的成績
avg_grade = {"國文": [], "數學": [], "英文": []}

# 3. 逐一取出每一位同學的成績，並加總到對應的科目
for sudjuct in subjects:  # 第一回合subjuct = "國文"
    for name, subject in grade.items():  # 第一回合每個人的"國文"成績串接
        avg_grade[sudjuct] += subject[sudjuct]

# 4. 計算各科目的平均成績
for subject, scores in avg_grade.items():
    avg = sum(scores) / len(scores)
    print(f"{subject} 的平均成績: {avg}")

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
