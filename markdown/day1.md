# Python 課程筆記

## 註解與快捷鍵
- `#` 用於註解，不會被執行。
- `CTRL + ?` 可以對選取範圍進行快速註解/取消註解。

## `print()` 函式
`print()` 用於在終端機顯示文字。

```python
print("Hello World")
```

## 基本型態 (Data Types)
Python 主要有以下幾種基本型態：

```python
print(1)        # int (整數)
print(1.0)      # float (浮點數)
print(1.234)    # float (浮點數)
print("apple")  # str (字串)
print(True)     # bool (布林值)
print(False)    # bool (布林值)
```

### 運算與字串拼接
```python
print(1 + 1)        # 2，數字加法
print("1" + "1")    # "11"，字串加法是字串拼接
```

## 變數 (Variables)
變數用於儲存數據，`=` 是指將右側的值賦予左側的變數。

```python
a = 10  # 宣告變數 a，賦值為 10
print(a)  # 印出 a 的值

a = "apple"  # 變數 a 重新賦值為 "apple"
print(a)  # 印出 a 的值
```

## 算術運算 (Arithmetic Operations)

```python
print(1 + 1)  # 加法
print(1 - 1)  # 減法
print(1 * 1)  # 乘法
print(1 / 1)  # 除法
print(1 // 1) # 整數除法
print(1**1)   # 次方
print(1 % 1)  # 取餘數
```

## 運算優先順序 (Operator Precedence)
1. `()` 括號
2. 乘 `*`、除 `/`、次方 `**`
3. 加 `+`、減 `-`
4. 比較運算符號
5. 邏輯運算符號
6. 位元運算

## 字串 (String)
字串是由文字組成的資料類型。

```python
s = "apple"  # 宣告字串變數 s
s = "apple"  # 重新宣告 (內容相同)
```
