# 這是流程控制的範例檔案 

# --- if 語句範例 --- 
print("--- if 語句範例 ---")

number = 10

if number > 5: # 判斷 number 是否大於 5
	print("這個數字大於 5") # 注意這裡有縮排
	
# --- if-else 語句範例 --- 
print("\n--- if-else 語句範例 ---")

score = 75

if score >= 60: # 如果分數大於或等於 60
	print("你及格了！")
else: # 否則 (分數小於 60)
	print("你不及格，請再加油。")

# 改變分數再測試一次
score = 50

if score >= 60:
	print("你及格了！ (再次測試)")
else:
	print("你不及格，請再加油。 (再次測試)")
	
print("\n--- if-elif-else 語句範例：成績評級 ---")

grade = 85

if grade >= 90:
	print("成績等級：A")
elif grade >= 80:         # 如果不是 A (即 <90)，再判斷是否 >= 80
	print("成績等級：B")
elif grade >= 70:         # 如果不是 A 也不是 B (即 <80)，再判斷是否 >= 70
	print("成績等級：C")
else:                     # 如果以上都不是 (即 <70)
	print("成績等級：D")

# 再次測試不同的分數 
grade = 65 
print(f"\n測試分數 {grade}:") 

if grade >= 90: 
	print("成績等級：A") 
elif grade >= 80: 
	print("成績等級：B") 
elif grade >= 70: 
	print("成績等級：C") 
else: 
	print("成績等級：D")

grade = 95 
print(f"\n測試分數 {grade}:") 

if grade >= 90: 
	print("成績等級：A") 
elif grade >= 80: 
	print("成績等級：B") 
elif grade >= 70: 
	print("成績等級：C") 
else: 
	print("成績等級：D")
	
# --- for 迴圈範例：使用 range() --- 
print("\n--- for 迴圈範例：使用 range() ---")

# 範例 1：從 0 到 4
print("從 0 到 4：")
for i in range(5): # range(5) 會產生 0, 1, 2, 3, 4
	print(i)

# 範例 2：從 1 到 5
print("從 0 到 5：")
for num in range(0, 6): # range(1, 6) 會產生 1, 2, 3, 4, 5
	print(num)

# 範例 3：偶數 (從 2 到 10，每次跳 2) 
print("\n從 2 到 10 的偶數:")
for even_num in range(2, 11, 2): # range(2, 11, 2) 會產生 2, 4, 6, 8, 10
	print(even_num)

# --- for 迴圈範例：遍歷列表 --- 
print("\n--- for 迴圈範例：遍歷列表 ---")

fruits = ["apple", "banana", "cherry"]

# 遍歷水果列表，每次迴圈將取得一個水果名稱
print("我喜歡的水果有：")
for fruit in fruits:
	print(fruit)

# 範例：計算列表元素的總和
numbers = [10, 20, 30, 40, 50]
total = 0 # 初始化總和變數

print(f"\n計算 {numbers} 的總和：")
for num in numbers:
	total = total + num # 每次迴圈將當前數字加到 total 中
	# 也可以寫作 total += num (這是它的簡寫形式)
print(f"總和是： {total}")

# --- while 迴圈範例：倒數計時 --- 
print("\n--- while 迴圈範例：倒數計時 ---")

count = 5

while count > 0: # 只要 count 大於 0，就繼續執行
	print(f"倒數計時： {count}")
	count = count - 1 # 每次迴圈讓 count 減 1，讓它最終能變成 0
	# 也可以寫作 count -= 1 (這是它的簡寫形式)

print("發射！")

# 另一個 while 迴圈範例：直到滿足條件為止
print("\n--- while 迴圈範例：密碼猜測 (簡單模擬) ---")
password = "open"
user_input = ""

print("請輸入密碼 (提示： open)")
while user_input != password: # 只要使用者輸入不等於密碼，就繼續要求輸入
	user_input = input("輸入密碼：") # input() 函式會讓程式暫停，等待使用者輸入
	if user_input != password:
		print("密碼錯誤，請重新輸入。")

print("密碼正確，歡迎進入！")