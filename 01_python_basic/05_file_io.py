# --- 檔案操作 - 寫入檔案範例 --- 
print("\n--- 檔案操作 - 寫入檔案範例 ---")

file_name = "my_first_file.txt" # 我們將要創建的檔案名稱

# 使用 'w' 模式寫入檔案 (如果檔案不存在會創建，如果存在會清空)
print(f"正在使用 'w' 模式寫入檔案： {file_name}")
with open(file_name, 'w', encoding='utf-8') as f:
	f.write("哈囉，這是我的第一個檔案操作範例！\n")
	f.write("我很喜歡學習 Python。\n")
	f.write("這是檔案的第三行。\n")
print(f"檔案 '{file_name}' 寫入完成。請檢查資料夾。")

# 使用 'a' 模式附加內容到檔案 (如果檔案不存在會創建，如果存在會附加)
print(f"\n正在使用 'a' 模式附加內容到檔案： {file_name}")
with open(file_name, 'a', encoding='utf-8') as f:
	f.write("這是新附加的第四行。\n")
	f.write("附加模式不會清空原有內容。\n")
print(f"檔案 '{file_name}' 附加完成。請再次檢查資料夾")

# 再次使用 'w' 模式寫入，觀察檔案內容是否被清空
new_file_name = "overwrite_test.txt"
print(f"\n正在使用 'w' 模式寫入檔案： {new_file_name} (此檔案會被清空或創建)")
with open(new_file_name, 'w', encoding='utf-8') as f:
	f.write("這是一行新的內容。\n")
print(f"檔案 '{new_file_name}' 寫入完成。")

print(f"\n正在使用 'w' 模式再次寫入檔案： {new_file_name} (內容將會被覆蓋)")
with open(new_file_name, 'w', encoding='utf-8') as f:
	f.write("這句話會覆蓋前面的內容。\n")
print(f"檔案 '{new_file_name}' 再次寫入完成。請檢查內容是否被覆蓋。")

# --- 檔案操作 - 讀取檔案範例 --- 
print("\n--- 檔案操作 - 讀取檔案範例 ---")

read_file_name = "my_first_file.txt"

# 檢查檔案是否存在 (這是個好習慣)
import os
if not os.path.exists(read_file_name):
	print(f"錯誤：檔案 '{read_file_name}' 不存在，無法讀取。請確保它在同一個資料夾。")
else:
	print(f"\n正在讀取檔案： {read_file_name}")

	# 1. 使用 read() 讀取整個檔案
	print("\n--- 使用 read() 讀取整個檔案 ---")
	with open(read_file_name, 'r', encoding='utf-8') as f:
		content = f.read()
		print(content)
	print("read() 讀取完成。")

	# 2. 使用 readline() 逐行讀取 
	print("\n--- 使用 readline() 逐行讀取 ---")
	with open(read_file_name, 'r', encoding='utf-8') as f:
		line1 = f.readline()
		line2 = f.readline()
		line3 = f.readline()
		print(f"第一行： {line1.strip()}") # .strip() 用來移除行尾的換行符
		print(f"第二行： {line2.strip()}")
		print(f"第三行： {line3.strip()}")
	print("readline() 讀取完成。")

	# 3. 使用 readlines() 讀取所有行到列表中 
	print("\n--- 使用 readlines() 讀取所有行到列表中 ---")
	with open(read_file_name, 'r', encoding='utf-8') as f:
		lines_list = f.readlines()
		print(f"讀取到的行列表 (原始包含換行符)： {lines_list}")
		# 遍歷列表並印出，移除換行符
		print("\n印出處理後的每行內容：")
		for line in lines_list:
			print(line.strip())
	print("readlines() 讀取完成。")

	# 4. 逐行迭代檔案 (最推薦的方法之一)
	print("\n--- 逐行迭代檔案範例 ---")
	with open(read_file_name, 'r', encoding='utf-8') as f:
		for line_num, line in enumerate(f, 1): # enumerate 可以同時得到行號和內容
			print(f"第 {line_num} 行 (迭代)： {line.strip()}")
	print("逐行迭代讀取完成。")

# 範例 1：使用 write() 寫入多行文字，手動添加換行符
file_name = "example_write.txt"
with open(file_name, 'w', encoding='utf-8') as f:
	f.write("這是第一行內容。\n") # 手動添加換行符
	f.write("這是第二行內容，手動換行。\n")
	f.write("這是第三行，沒有換行，所以下一句會皆在後面")
	f.write("這句話會緊跟在第三行後面，因為上面沒有 '\\'。")

print(f"檔案 '{file_name}' 寫入完成，請檢查內容。")

# 範例 2：使用 writelines() 寫入列表中的多行文字
print("\n--- 使用 writelines() 寫入列表中的多行文字 ---")

file_name_2 = "example_writelines.txt"
lines_to_write = [
	"第一行內容。\n"
	"第二行，也是手動換行。\n"
	"第三行，然後沒有換行" # 這行沒有換行符
]

with open(file_name_2, 'w', encoding='utf-8') as f:
	f.writelines(lines_to_write)
	f.write("這句話會緊接在第三行後面。") # 因為第三行沒有換行，這句會接著寫

print(f"檔案 '{file_name_2}' 寫入完成，請檢查內容。")

# --- 檔案操作 - 基礎 CSV 檔案讀寫範例 --- 
print("\n--- 檔案操作 - 基礎 CSV 檔案讀寫範例 ---")

csv_file_name = "my_simple_data.csv"

# 寫入一個簡單的 CSV 檔案 
print(f"\n正在寫入基礎 CSV 檔案: {csv_file_name}")
with open(csv_file_name, 'w', encoding='utf-8') as f:
	f.write("Name,Age,City\n") # 標題行
	f.write("Alice,25,New York\n")
	f.write("Bob,30,London\n")
	f.write("Charlie,22,Paris\n")
print(f"檔案 '{csv_file_name}' 寫入完成。")

# 讀取這個簡單的 CSV 檔案
print(f"\n正在讀取基礎 CSV 檔案: {csv_file_name}")
with open(csv_file_name, 'r', encoding='utf-8') as f:
	# 逐行讀取併分割
	for line_num, line in enumerate(f, 1):
		stripped_line = line.strip() # 移除行尾換行符
		values = stripped_line.split(',') # 以逗號分割字串

		if line_num == 1: # 如果是第一行 (標題行)
			print(f"CSV 標題： {values}")
		else: # 數據行
			print(f"數據行 {line_num-1}: 姓名={values[0]}, 年齡={values[1]}, 城市={values[2]}")
print(f"檔案 '{csv_file_name}' 讀取完成。")

# --- 錯誤處理：FileNotFoundError 範例 ---
print("\n--- 錯誤處理：FileNotFoundError 範例 ---")
non_existent_file = "non_existent_file.txt"

try:
	with open(non_existent_file, 'r', encoding='utf-8') as f:
		content = f.read()
		print(f"檔案內容： {content}")
except FileNotFoundError:
	print(f"錯誤：檔案 '{non_existent_file}' 不存在。")
	print("請確認檔案名稱和路徑是否正確。")
except Exception as e: # 捕獲其他所有可能發生的錯誤
	print(f"發生了其他未預期的錯誤：{e}")

print("程式繼續執行 (即使檔案不存在，程式也沒有崩潰)。")