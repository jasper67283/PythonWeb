# 字串格式化
name = "apple"
age = 18
print(f"Hello,my name is (name) , I am (age) years old")  # f-string
# 可以將變數或其他型態的資料放到f字串裡面的{},這樣就可以在字串中顯示

print(len("apple"))  # len函式式可以取得字串的長度
print(len("，"))  # len函式式可以計算字串的長度
# type() 函式可以查看變數的型態
print(type(1))  # <class 'int'>
print(type("apple"))  # <class 'str'>
print(type(1.0))  # <class 'float'>
print(type(True))  # <class 'bool'>

# 型態轉換
print(int(1.0))  # float轉換成int
print(float("1"))  # int轉換成float
print(str(1))  # int轉換成str
print(str(1.234))  # float轉換成str
print(bool(1))  # int轉換成bool
print(bool("1"))  # str轉換成bool
print(bool(1.234))  # float轉換成bool
print(float("1.234"))  # str轉換成float
print(bool(1.234))  # float轉換成bool
# print(int("hello")) # 這行程式會报錯,因為字串不是數字


print("輸入開始")
# input() 函式可以讀取輸入
# ()裡面的文字式提示訊息會顯示在終端機才會等待輸入
a = input("請輸入一些文字:")
print("輸入結束")
print(int(a) * int(a))
print(type(a))  # 證明透過input()輸入內容都是字串
a = int(a)
print(type(a))  # 這時候a已經式整數了
# 比較運算子
print(1 == 1)  # True
print(1 != 1)  # False
print(1 > 1)  # False
print(1 < 1)  # False
print(1 >= 1)  # True
print(1 <= 1)  # True
# 邏輯運算子
# and 運算子
print(True and True)  # 同時為真
print(True and False)  # 同時為假
print(False and False)  # 同時為假

# or 運算子
print(True or True)  # 同時為真
print(True or False)  # 同時為真
print(False or False)  # 同時為假

# or 運算子
print(not True)  # 同時為假
print(not False)  # 同時為真

# 優先順序
# 1. ( ) 誇號
# 2. ** 次方
# 3. + - 加減
# 4. * / // 整數除法
# 5. == != > < >= <= 字串比較
# 6. and or 邏輯運算子
