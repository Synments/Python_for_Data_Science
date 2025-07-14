# 這是函式的範例檔案 
# --- 函式 (Functions) - 簡單範例 --- 
print("--- 函式 (Functions) - 簡單範例 ---") 

# 定義一個沒有參數，也沒有回傳值的函式
def greet():
	print("哈囉，歡迎來到 Python 的世界！")
	print("很高興能和您一起學習函式！")

# 呼叫 (Call) 函式 
# 函式定義後並不會立即執行，需要呼叫它才會執行
print("第一次呼叫 greet() 函式：")
greet()

print("\n第二次呼叫 greet() 函式：")
greet()

# 定義一個帶有參數的函式
def greet_user(name): # name 就是一個參數
	print(f"哈囉，{name}！")
	print("很高興見到您。")

# 呼叫帶有參數的函式，並傳遞引數 (Argument)
print("\n呼叫 greet_user() 函式：")
greet_user("Sean") # "Sean" 就是傳遞給 name 參數的引數
greet_user("Alice") # 可以重複使用，傳遞不同的引數

# 定義一個帶有參數和回傳值的函式
def add_numbers(a, b): # a 和 b 是參數
	sum_result = a + b
	return sum_result # 回傳計算結果

# 呼叫帶有回傳值的函式，並將結果儲存到變數中
print("\n呼叫 add_numbers() 函式：")
result1 = add_numbers(5, 3) # 5 和 3 是引數
print(f"5 + 3 = {result1}")

result2 = add_numbers(100, 200)
print(f"100 + 200 = {result2}")

# --- 函式參數與引數範例 --- 
print("\n--- 函式參數與引數範例 ---") 

# 1. 位置引數 (Positional Arguments) 
# 函式定義時有兩個參數：item 和 price
def describe_product(item, price):
	print(f"這個產品是 {item}，價格是 ${price}。")

print("\n使用位置引數呼叫函式：")
describe_product("筆記型電導", 1200) # "筆記型電腦" 賦值給 item, 1200 賦值給 price
describe_product("滑鼠", 25)

# 2. 關鍵字引數 (Keyword Arguments) 
# 呼叫函式時，明確指定參數名來傳遞引數
print("\n使用關鍵字引數呼叫函式：")
describe_product(price=1500, item="手機") # 順序可以不同，但名稱要對應
describe_product(item="鍵盤", price=75)

# 3. 預設參數值 (Default Parameter Values) 
# 定義函式時，為參數設定一個預設值
def send_email(to_address, subject="無主題", body=""): # subject 和 body 有預設值
	print(f"\n寄送郵件給： {to_address}")
	print(f"主題： {subject}")
	print(f"內容： {body}")
	print("---")
	
print("\n使用預設參數值呼叫函式:")
send_email("sean@example.com") # 只提供 to_address，subject 和 body 使用預設值
send_email("bob@example.com", subject="會議通知") # 提供 to_address 和 subject，body 使用預設值
send_email("alice@example.com", subject="問候", body="希望您一切都好！") # 提供所有引數

# --- 函式回傳值與區域變數範例 --- 
print("\n--- 函式回傳值與區域變數範例 ---")

# 1. 函式回傳值
def calculate_erea(length, width):
	area = length * width # area 是區域變數
	return area # 回傳計算出的面積

# 呼叫函式並使用回傳值
room_area = calculate_erea(5, 8)
print(f"房間面積： {room_area} 平方公尺")

def divide(numerator, denominator):
	if denominator == 0:
		print("錯誤：除數不能為零！")
		return None # 遇到錯誤時回傳 None
	else:
		return numerator / denominator # 正常回傳結果

print(f"10 / 2 = {divide(10, 2)}")
print(f"10 / 0 = {divide(10, 0)}")

# 2. 函式內部變數 (區域變數)
def my_function():
	local_var = "我是一個區域變數"
	print(local_var)

my_function() # 函式內部可以訪問 local_var

# 嘗試從函式外部訪問區域變數 (會報錯) 
# print(local_var) # 解除註解會報錯：NameError: name 'local_var' is not defined

# --- 可變數量引數 (*args) 和 關鍵字引數 (**kwargs) 範例 --- 
print("\n--- 可變數量引數 (*args) 和 關鍵字引數 (**kwargs) 範例 ---") 

# 1. 使用 *args 接收可變數量的位置引數
def calculate_total(*prices): # prices 會是一個元組
	total = 0
	print(f"收到的 prices (元組)： {prices}")
	for price in prices:
		total += price
	return total

print("\n使用 *args 計算總和：")
print(f"購物車總價 (無商品)： {calculate_total()}")
print(f"購物車總價 (單一商品 100)： {calculate_total(100)}")
print(f"購物車總價 (多個商品 10, 20, 30)： {calculate_total(10, 20, 30)}")

# 2. 使用 **kwargs 接收可變數量的關鍵字引數
def print_profile(**details): # details 會是一個字典
	print(f"收到的 details (字典)： {details}")
	for key, value in details.items():
		print(f"{key.replace('_', ' ').title()}： {value}") # 讓輸出更美觀

print("\n使用 **kwargs 列印個人資料：")
print_profile(name="Sean", age=30, city="Taipei")
print("-" * 20)
print_profile(product_name="Laptop", price=1200, category="Electronics")

# 3. 結合使用一般參數、*args 和 **kwargs (順序很重要！) 
# 順序必須是：一般參數, *args, **kwargs 
def complex_function(required_arg, *args, **kwargs): 
	print(f"\n必填引數: {required_arg}") 
	print(f"額外位置引數 (*args): {args}") 
	print(f"額外關鍵字引數 (**kwargs): {kwargs}") 

print("\n結合使用範例:") 
complex_function("我是必填", 1, 2, 3, item="apple", color="red") 
print("-" * 20) 
complex_function("只有必填")