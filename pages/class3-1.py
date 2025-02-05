# for 迴圈
# for 會搭配in來使用,in後面接一個有範圍的東西
# range(5)可以產生0到4的數字,不包含5,如果想包含5就加1
# i 是迴圈的變數可以自己取,迴圈變數只能在迴圈裡面使用
# 迴圈變數每回合會從範圍裡面取一個資料出來
for i in range(5):
    print(i)

# range 可以設定起始值與結束值,但是不會包含結束值
# range(1,5)可以產生1到4的數字,不包含5
for i in range(1, 5):
    print(i)

# range 可以設定起始值與、結束值與間隔值,但是不會包含結束值
# range(1,10,2)可以產生1,3,5,7,9的數字,不包含10
for i in range(1, 10, 2):
    print(i)

# 補充random.randrange()函數
# random.randrange()函數可以產生一個指定範圍內的隨機數
# random.randrange()設定傳入的參數跟range一樣
import random

for i in range(1, 10):
    print(random.randrange(1, 10))

# List 列表\清單\陣列
print([])  # 空的列表
print([1, 2, 3])  # 這是一個有3個元素的列表
print([1, 2, 3, "a", "b", "c"])  # 這是一個有6個元素的列表
print([[1, 2, 3, "a", "b", "c"]])  # 這是一個有4個元素的列表
print([1, True, "a", 1.23])  # 這是一個有4個元素的列表

# list 讀取元素，元素的index從0開始
L[1, 2, 3, "a", "b", "c"]
print(L[0])  # 取出第一個元素
print(L[1])  # 取出第二個元素
print(L[2])  # 取出第三個元素
print(L[3])  # 取出第四個元素"a"

# list 取長度，也就是list中有幾個元素，不是index的最大值
L = [1, 2, 3, "a", "b", "c"]
print(len(L))  # 6

# list 走訪元素
# 可以透過取出index的方式來找到list中的資料
# 也可以直接把list當作一個範圍來取得資料
# 這兩種方式都可以,但是看使用的情境是否會需要index來決定要用哪一種方式
L = [1, 2, 3, "a", "b", "c"]

for i in range(len(L)):
    print(L[i])  # 1,2,3,"a","b","c"

for i in range(0, len(L), 2):  # 0, 2, 4
    print(L[i])  # 1,3,"b"

for i in l:
    print(i)  # 1,2,3,"a","b","c"

R = [1, 2, 3, "a", "b", "c"]
# 就是取index 0到最後，每次取2個元素，所以是[1, 3, "b"]
print(R[::2])
# 就是取indox 1到3的元素，不包含index 4，所以是[2, 3, "a"]
print(R[1:4])
# 就是取index 1到3的元素，不包含index 4，並且每次取2個元素，所以是[2, "a"]
print(R[1:4:2])
# 跟range一樣的用法，只是符號不同

# list修改元素
R = [1, 2, 3, "a", "b", "c"]
R[0] = 2
print(R)  # [2, 2, 3, "a", "b", "c"]

# call by value
a = 1
b = a  # 複製a的值給b
b = 2
print(a, b)

# call by reference
a = [1, 2, 3]
b = a  # 把a跟b指向同一個記憶體位置，所以改變b的值，a也會跟著改變
b[0] = 2
print(a, b)

a = [1, 2, 3]
b = a.copy()  # 把a的值複製到b，所以改變b的值，a不會跟著改變
b[0] = 2
print(a, b)

# list的append
L = [1, 2, 3]
L.append(4)  # 在L的最後面加一個元素4
print(L)  # [1, 2, 3, 4]

# list的移除元素方式有兩種
# 1. 使用remove，可以移除指定的元素
L = ["a", "b", "c", "d", "a"]
L.remove("a")  # 移除第一個a，["b", "c", "d", "a"]
# 代表remove會從頭開始找，找到第一個符合條件的元素就會移除
# 如果沒有符合條件的元素，可以用迴圈找到
for i in L:
    if i == "a":
        L.remove(i)  # L.remove(i)

# 2. 使用pop，可以移除指定的index元素
L = ["a", "b", "c", "d", "a"]
L.pop(0)  # 移除index 0的元素，["b", "c", "d", "a"]
# 代表pop會移除指定的index元素，不會從頭開始找
# 如果不指定index，則會移除最後一個元素
L.pop()  # 移除最後一個元素
print(L)
