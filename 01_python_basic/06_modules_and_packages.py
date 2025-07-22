# --- 導入自定義的 my_module 範例 (第一部分) ---
print("\n--- 導入自定義的 my_module 範例 (第一部分) ---")

# 1. 導入整個 my_module
print("\n--- 導入整個 'my_module' ---")
import my_module

# 訪問模組中的變數 (需要加上 my_module. 前綴)
print(f"從 my_module 導入的問候語： {my_module.GREETING}")
print(f"從 my_module 導入的 PI 近似值： {my_module.PI_APPROX}")

# 呼叫模組中的函式 (需要加上 my_module. 前綴)
my_name = "Sean"
print(f"my_module 的問候： {my_module.greet(my_name)}")
print(f"my_module 的加法： 10 + 5 = {my_module.add(10, 5)}")

# --- 導入自定義的 my_module 範例 (第二部分 - 導入特定功能) --- 
print("\n--- 導入自定義 my_module 範例 (第二部分 - 導入特定功能) ---")

# 2. 從 my_module 導入特定函式 (greet 和 multiply)
print("\n--- 從 'my_module' 導入特定函式 'greet' 和 'multiply' ---")
from my_module import greet, multiply

# 直接使用導入的函式名稱，不需要前綴
print(f"直接呼叫 greet 函式： {greet('Python 學習者')}")
print(f"直接呼叫 multiply 函式： 6 * 7 = {multiply(6, 7)}")

# --- 導入自定義的 my_module 範例 (第三部分 - 導入並重新命名) --- 
print("\n--- 導入自定義的 my_module 範例 (第三部分 - 導入並重新命名) ---")
from my_module import GREETING as MY_GREETING

# 使用新的名稱訪問變數
print(f"重新命名的問候語: {MY_GREETING}")

# 嘗試訪問原始的 GREETING 會報錯 (NameError)，因為沒有直接導入原始名稱 
# print(GREETING) # 如果取消註釋這行會導致 NameError，可以試著取消註釋再執行看看效果 
# 因為在前面已經 `import my_module` 了，所以這裡仍然可以透過模組前綴訪問原始的 GREETING 
# 如果沒有 `import my_module`，則這行會報錯
print(f"原始模組名稱訪問的問候語 (已透過 my_module.GREETING)： {my_module.GREETING}")

# --- 導入所有功能範例 (不推薦) --- 
print("\n--- 導入所有功能範例 (不推薦) ---") 

# 4. 從 my_module 導入所有內容 (*) 
# 請注意：這在實際專案中通常不推薦使用，除非非常清楚自己在做什麼。 
print("\n--- 從 'my_module' 導入所有內容 (*) ---") 
from my_module import * 

# 現在可以直接使用模組中的變數和函式，不需前綴 
# 但這讓程式碼來源不那麼明確 
print(f"直接使用的問候語: {GREETING}") # 直接使用 GREETING 
print(f"直接呼叫 add 函式: 7 + 8 = {add(7, 8)}") # 直接使用 add 
print(f"直接呼叫 multiply 函式: 9 * 4 = {multiply(9, 4)}") # 直接使用 multiply 

# 由於前面已經 `import my_module` 了，所以 `my_module.GREETING` 仍然有效。 
# 但如果沒有前面的 `import my_module`，`my_module.GREETING` 就會失效。 
print(f"再次透過 my_module.GREETING 訪問: {my_module.GREETING}")

# --- 標準函式庫模組探索範例 --- 
print("\n--- 標準函式庫模組探索範例 ---") 

# 範例 1: 使用 math 模組 (之前已經用過它了)
print("\n--- 使用 math 模組 ---")
import math
print(f"圓周率 (math.pi)： {math.pi}")
print(f"2 的 3 次方 (math.pow)： {math.pow(2, 3)}") # 等同於 2**3

# 範例 2: 使用 datetime 模組 
print("\n--- 使用 datetime 模組 ---") 
import datetime # 取得當前日期和時間

now = datetime.datetime.now()
print(f"目前的日期和時間： {now}")
print(f"年份： {now.year}")
print(f"月份： {now.month}")
print(f"日期： {now.day}")

# 範例 3: 使用 help() 和 dir() 探索模組
print("\n--- 使用 help() 和 dir() 探索模組 ---")
print("\n### dir(math) 的結果 (部分顯示) ###")
# dir(math) 會顯示 math 模組中所有可用的名稱
# 這裡只顯示前 10 個，因為列表可能很長
print(dir(math)[:10])

print("\n### help(math.sqrt) 的結果 (部分顯示) ###") 
# help(math.sqrt) 會顯示 sqrt 函式的詳細說明 
# 實際執行時會顯示更多，這裡為了範例只提示會出現說明 
# help(math.sqrt) # 取消註釋這行，並在終端機中按 'q' 退出說明介面
print("(在終端機中執行 help(math.sqrt) 會顯示詳細說明，按 'q' 退出)")

# 範例：導入 my_package 套件中的 greeting_module
import my_package.greeting_module

# 呼叫 greeting_module 中的函式
message = my_package.greeting_module.say_hello("World")
print(message)

# --- 導入自定義套件 (my_package) 範例 --- 
print("\n--- 導入自定義套件 (my_package) 範例 ---") 

# 1. 導入套件中的特定模組
print("\n--- 導入 'my_package.greeting_module' ---")
import my_package.greeting_module

# 訪問模組中的函式
package_hello = my_package.greeting_module.say_hello("Alice")
print(f"從套件模組呼叫： {package_hello}")

# 2. 從套件中的模組導入特定功能
print("\n--- 從 'my_package.greeting_module' 導入 'say_goodbye' ---")
from my_package.greeting_module import say_goodbye

# 直接使用導入的函式
package_goodbye = say_goodbye("Bob")
print(f"直接呼叫套件模組中的函式： {package_goodbye}")

# 3. 從套件中的模組導入特定功能並重新命名
print("\n--- 從 'my_package.greeting_module' 導入 'say_hello' 並重新命名為 'greet_package' ---")
from my_package.greeting_module import say_hello as greet_package

# 使用新的名稱呼叫函式
renamed_greet = greet_package("Charlie")
print(f"使用重新命名的套件函式： {renamed_greet}")

# --- 第三方套件安裝與使用範例 --- 
print("\n--- 第三方套件安裝與使用範例 ---")

# 導入 requests 套件
import requests

# 嘗試從網站獲取數據 
print("\n--- 使用 requests 套件獲取網頁內容 ---")
try:
	# 嘗試獲取 Google 網站的內容
	response = requests.get("https://www.google.com.tw")
	# 檢查請求是否成功 (狀態碼 200 表示成功)
	if response.status_code == 200:
		print(f"成功獲取網頁內容！狀態碼： {response.status_code}")
		# 為了避免輸出太多內容，這裡只印出內容的前 200 個字元
		print(f"部分網頁內容 (前 200 字元)： \n{response.text[200]}...")
	else:
		print(f"獲取網頁內容失敗。狀態碼： {response.status_code}")
except requests.exception.ConnectionError as e:
	print(f"錯誤：無法連接到網際網路或目標網站。請檢查您的網路連線。錯誤訊息： {e}")
except Exception as e:
	print(f"發生了其他錯誤： {e}")
	
