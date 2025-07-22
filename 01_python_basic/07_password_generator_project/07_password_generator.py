# 07_01_password_generator.py

import random # 導入 random 模組，用於生成隨機數

# 定義密碼可能包含的字元集
# 數字
digits = '0123456789'
# 小寫字母
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
# 大寫字母
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# 特殊符號
symbols = '!@#$%^&*()_+-=[]{}|;:,.<>/?'

print("密碼生成器已準備就緒！")

# 獲取使用者輸入
print("\n--- 請輸入您的密碼要求 ---")
# 詢問密碼長度
# input() 函式會獲取使用者的輸入，它總是回傳字串，所以我們用 int() 轉換成整數
password_length = int(input("請輸入密碼長度 (建議 8-16 個字元)："))

# 詢問是否包含數字
# 使用 lower() 將輸入轉換為小寫，方便判斷
include_digits = input("是否包含數字？ (y/n): ").lower() == 'y'
# 詢問是否包含小寫字母
include_lowercase = input("是否包含小寫字母？ (y/n): ").lower() == 'y'
# 詢問是否包含大寫字母
include_uppercase = input("是否包含大寫字母？ (y/n): ").lower() == 'y'
# 詢問是否包含特殊符號
include_symbols = input("是否包含特殊符號？ (y/n): ").lower() == 'y'

print("您的設定已接收")

# 根據使用者的選擇，建立可用字元池 
# 初始時，可用字元池是空的
available_characters = ''

# 如果使用者選擇包含數字，就把數字字元集加到可用字元池中
if include_digits:
	available_characters += digits

# 如果使用者選擇包含小寫字母，就把小寫字母字元集加到可用字元池中
if include_lowercase:
	available_characters += lowercase_letters

# 如果使用者選擇包含大寫字母，就把大寫字母字元集加到可用字元池中
if include_uppercase:
	available_characters += uppercase_letters

# 如果使用者選擇包含特殊符號，就把特殊符號字元集加到可用字元池中
if include_symbols:
	available_characters += symbols

# 檢查是否至少選擇了一種字元類型，如果都沒有選，就顯示錯誤訊息並退出
if not available_characters:
	print("錯誤：您必須至少選擇一種字元類型來生成密碼。")
	exit() # 退出程式
else:
	print(f"可用字元池已建立，共有 {len(available_characters)} 種字元。")
	# 為了避免輸出過多，這裡只印出可用字元池的前20個字元和後20個字元 
	# 如果 available_characters 不足40個字元，就全部印出
	if len(available_characters) > 40:
		print(f"部分可用字元： {available_characters[:20]}...{available_characters[-20:]}")
	else:
		print(f"所有可用字元： {available_characters}")
		
    # 生成密碼
generated_password = [] # 使用列表來儲存每個密碼字元，方便添加

# 迴圈指定密碼長度次數
for _ in range(password_length):
	# 從 available_characters 中隨機選擇一個字元 
	# random.choice() 函式會從給定的序列 (字串、列表、元組) 中隨機選擇一個元素
	random_char = random.choice(available_characters)
	# 將隨機選擇的字元添加到 generated_password 列表中
	generated_password.append(random_char)

# 將列表中的字元連接起來，形成最終的密碼字串 
# .join() 方法用於將列表中的所有字串元素連接成一個單一字串 
# 這裡使用空字串 '' 作為連接符，表示直接連接，中間不加任何東西
final_password = "".join(generated_password)

# 顯示生成的密碼
print("\n--- 您的密碼已生成 ---")
print(f"生成的密碼： {final_password}")
