# my_module.py 這是我的第一個自定義模組 
# 模組中的變數
GREETING = "哈囉，我是來自 my_module 的問候！"
PI_APPROX = 3.14159

# 模組中的函示
def greet (name):
	"""簡單的問候函式"""
	return f"{GREETING} 很高興見到您，{name}！"

def add(a, b):
	"""計算兩個數字的和"""
	return a + b

def multiply(a, b):
	"""計算兩個數字的積"""
	return a * b

# 這段程式碼只有在直接運行 my_module.py 時才會執行 
# 如果是作為模組被匯入，這段程式碼不會執行
if __name__ == "__main__":
	print("--- 正在直接運行 my_module.py ---")
	print(f"模組內的 GREETING: {GREETING}")
	print(f"模組內的 PI_APPROX: {PI_APPROX}")
	print(greet("測試者"))
	print(f"5 + 3 = {add(5, 3)}")
	print(f"5 * 3 = {multiply(5, 3)}")
	print("--- my_module.py 直接運行結束 ---")
