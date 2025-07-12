# 這是我的第一個變數範例

# 變數用來儲存單一的資料
my_age = 30 # 將數字 30 儲存到變數 my_age 中
print(my_age) # 使用 print() 函式將變數的值印出來

# 變數的值可以改變
my_age = 31 # my_age 現在儲存了新的值
print(my_age)

# 變數可以儲存不同型別的資料
my_name = "Sean" # 字串 ( 文字 )
my_height = 175.5 # 浮點數 ( 帶小數點的數字 )
is_student = True # 布林值 ( True 或 False )

print(my_name)
print(my_height)
print(is_student)

# --- 查看資料型別 --- 
print("\n--- 查看資料型別 ---") # 只是分隔線 

print(type(my_age)) # my_age 現在是 31 
print(type(my_name)) 
print(type(my_height)) 
print(type(is_student)) 

# 也可以直接查看資料的型別 
print(type(10)) 
print(type(3.14)) 
print(type("Hello")) 
print(type(False))

# --- 算術運算子範例 ---
print("\n--- 算術運算子範例 ---")

num1 = 10
num2 = 3

# 加法
print(f"num1 + num2 = {num1 + num2}")

# 減法
print(f"num1 - num2 = {num1 - num2}")

# 乘法
print(f"num1 * num2 = {num1 * num2}")

# 除法 (結果會是浮點數)
print(f"num1 / num2 = {num1 / num2}")

# 取餘數 (10 除以 3 的餘數是 1)
print(f"num1 % num2 = {num1 % num2}")

# 次方 (10 的 3 次方)
print(f"num1 ** num2 = {num1 ** num2}")

# 整數除法 (只取商的整數部分)
print(f"num1 // num2 = {num1 // num2}")

# --- 比較運算子範例 ---
print("\n--- 比較運算子範例 ---")

# 使用之前的 num1 = 10, num2 = 3
print(f"num1 == num2: {num1 == num2}") # 10 等於 3 嗎？
print(f"num1 != num2: {num1 != num2}") # 10 不等於 3 嗎？
print(f"num1 > num2: {num1 > num2}") # 10 大於 3 嗎？
print(f"num1 < num2: {num1 < num2}") # 10 小於 3 嗎？
print(f"num1 >= num2: {num1 >= num2}") # 10 大於或等於 3 嗎？
print(f"num1 <= num2: {num2 <= num2}") # 10 小於或等於 3 嗎？

# --- 邏輯運算子範例---
print("\n--- 邏輯運算子範例 ---")

is_sunny = True
is_weekend = False

# and 運算子
print(f"is_sunny and is_weekend: {is_sunny and is_weekend}") # 晴天且是周末嗎？

# or 運算子
print(f"is_sunny or is_weekend: {is_sunny or is_weekend}") # 晴天或是周末嗎？

# not 運算子
print(f"not is_sunny: {not is_sunny}") # 不是晴天嗎？

# --- 註解範例 --- 
print("\n--- 註解範例 ---") 

# 這是一個單行註解，用來解釋下一行程式碼的目的。 
# 這行程式碼會印出數字 7。 
my_lucky_number = 7 
print(my_lucky_number) # 你也可以在程式碼後面加上註解 

''' 
這是一個多行註解。 
它可以跨越多行，用來提供更詳細的說明。 
例如：這個區塊的程式碼是用來演示註解的用法。 
''' 

""" 你也可以用三個雙引號來創建多行註解。 
效果和三個單引號是一樣的。 
這通常用於函式或模組的文件說明。 
""" 

# print("這行程式碼被註解掉了，所以不會執行。")