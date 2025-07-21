# 任務 A：寫入個人資料到檔案
print("--- 任務 A：寫入個人資料到檔案 ---")
file_my_info = "my_info.txt"

with open(file_my_info, 'w', encoding='utf-8') as f:
    f.write("暱稱：Sean\n")
    f.write("居住地：Taipei\n")
    f.write("語言：Taiwanese\n")
print(f"個人資料： '{file_my_info}' 寫入完成")

# 任務 B：讀取 CSV 數據並印出

fruits_file = "fruits.csv" # 建議將變數名稱改為更具描述性的 `fruits_file`

# 創建一個簡單的 CSV 檔案 (如果它不存在的話)，方便測試
# 確保這個檔案包含了任務要求的內容

try:
    with open(fruits_file, 'w', encoding='utf-8') as f:
        f.write("Fruit,Color,Taste\n")
        f.write("Apple,Red,Sweet\n")
        f.write("Banana,Yellow,Sweet\n")
        f.write("Lemon,Yellow,Sour\n")
    print(f"已創建或更新測試檔案: {fruits_file}\n")
except Exception as e:
    print(f"創建或更新檔案時發生錯誤: {e}")

print("--- 任務 B：讀取 CSV 數據並印出 ---")

try:
    with open(fruits_file, 'r', encoding='utf-8') as f:
        # 使用 enumerate 從第 1 行開始計數
        for line_num, line in enumerate(f, 1):
            stripped_line = line.strip() # 移除行尾的換行符

            # 忽略空行
            if not stripped_line:
                continue

            values = stripped_line.split(',') # 以逗號分割字串

            if line_num == 1: # 處理標題行
                # print(f"CSV 標題: {values}") # 這行你可以選擇保留或移除
                # 我們可以儲存標題，方便後續引用
                headers = values
                print(f"CSV 標題已讀取: {', '.join(headers)}")
            else: # 處理數據行
                # 確保數據行有足夠的欄位以避免索引錯誤
                if len(values) >= 3:
                    # 按照任務要求，分開印出每個欄位的值
                    # 這裡使用 f-string 和索引來取出值
                    print(f"第 {line_num-1} 筆數據: 水果是：{values[0]}，顏色是：{values[1]}，味道是：{values[2]}")
                else:
                    print(f"警告: 第 {line_num} 行的欄位不足: {stripped_line}")

except FileNotFoundError:
    print(f"錯誤：檔案 '{fruits_file}' 不存在，無法讀取。請確保它在同一個資料夾。")
except Exception as e: # 捕獲其他所有可能發生的錯誤
    print(f"發生了其他未預期的錯誤：{e}")

print("\n逐行迭代讀取完成。")