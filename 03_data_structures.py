fruits = ["apple", "banana", "cherry", "date"]
print(f"水果列表： {fruits}")
print(f"型別： {type(fruits)}")

# 創建一個包含數字的列表
numbers = [1, 2, 3, 4, 5]
print(f"數字列表： {numbers}")

# 創建一個包含混合型別的列表
my_info = ["Sean", 30, True, 175.5]
print(f"我的資訊列表： {my_info}")

# 創建一個空列表
empty_list = []
print(f"空列表： {empty_list}")

# --- 訪問列表元素 (索引從 0 開始) --- 
print("\n--- 訪問列表元素 ---")

# 使用之前創建的水果列表
print(f"原始水果列表： {fruits}") # ['apple', 'banana', 'cherry', 'date']

print(f"第一個水果 (索引 0)： {fruits[0]}") # 訪問第一個元素
print(f"第三個水果 (索引 2)： {fruits[2]}") # 訪問第三個元素

# 使用我的資訊列表
print(f"我的資訊列表： {my_info}") # ['Sean', 30, True, 175.5]
print(f"我的名字： {my_info[0]}") # 訪問名字
print(f"我的身高： {my_info[3]}") # 訪問身高

# 使用複數索引
print(f"最後一個水果 (索引 -1)： {fruits[-1]}")
print(f"倒數第二個水果 (索引 -2)： {fruits[-2]}")

# --- 修改列表元素 --- 
print("\n--- 修改列表元素 ---") 

# 使用之前創建的水果列表
print(f"修改前的列表： {fruits}") # 假設是 ['apple', 'banana', 'cherry', 'date']

# 將第二個水果 (索引 1) 從 'banana' 改為 'orange'
fruits[1] = "orange"
print(f"修改索引 1 後的列表： {fruits}")

# 將我的資訊列表中的年齡 (索引 1) 從 30 改為 31
print(f"修改前的個人資訊： {my_info}")
my_info[1] = 31
print(f"修改年齡後： {my_info}")

# --- 列表的常見操作 (新增、刪除) --- 
print("\n--- 列表的常見操作 (新增、刪除) ---")


my_list = ["apple", "banana", "cherry"] 
print(f"原始列表: {my_list}")

# 1. 新增元素到列表末尾 (append())
# append() 方法會將一個新元素添加到列表的「最後面」。
my_list.append("date")
print(f"append 'date' 後： {my_list}")

# 2. 在指定位置插入元素 (insert(index, element))
# insert() 方法允許在指定索引位置插入一個新元素
# 後面的元素會自動往後移
my_list.insert(1, "grape") # 在索引 1 的位置插入 'grape'
print(f"insert 'grape' 在索引 1 後：{my_list}")

# 3. 刪除指定索引的元素 (del 語句)
# del 是一個 python 語句，可以用來刪除列表中的指定索引元素。
del my_list[0] # 刪除索引 0 的元素 (此時是 'apple')
print(f"del 索引 0 後：{my_list}")

# 4. 刪除指定值的元素 (remove(value))
# remove() 方法會刪除列表中「第一個」找到的指定值。
# 如果列表中有多個相同的值，它只會刪除第一個。
# 如果值不存在，會報錯。
my_list.remove("cherry") # 刪除列表中第一個 'cherry'
print(f"remove 'cherry' 後： {my_list}")

# 5. 移除並回傳最後一個元素 (pop())
# pop() 方法會移除列表中的「最後一個」元素，並將其回傳。
# 如果提供索引，它會移除並回傳指定索引的元素。
removed_item = my_list.pop() # 移除列表最後一個元素
print(f"pop() 移除了： {removed_item}")
print(f"pop() 後的列表： {my_list}")

# 使用 pop(index) 移除指定索引的元素
# curren_list: ['grape', 'date']
removed_specific_item = my_list.pop(0) # 移除索引 0 的 'grape'
print(f"pop(0) 移除了： {removed_specific_item}")
print(f"pop(0) 後的列表： {my_list}")

# --- 列表的常見操作 (查找、排序、複製、清空) --- 
print("\n--- 列表的常見操作 (查找、排序、複製、清空) ---")

# 1. 檢查元素是否存在 (in 關鍵字) 
# 'in' 關鍵字會回傳一個布林值 (True 或 False)，表示元素是否在列表中。
current_fruits = ["orange", "date"] # 承接上一個練習結束後的狀態
print(f"當前水果列表： {current_fruits}")
print(f"'orange' 是否在列表中？ {'orange' in current_fruits}") # True
print(f"'apple' 是否在列表中？ {'apple' in current_fruits}") # False

# 2. 獲取列表長度 (len() 函式)
# len() 是一個內建函式，回傳列表中元素的數量。
print(f"水果列表的長度： {len(current_fruits)}")

# 3. 排序列表 (sort())
# sort() 方法會「直接修改」原始列表，將其按照升序 (預設) 或降序排列。
numbers = [5, 2, 8, 1, 9]
print(f"\n原始數字列表： {numbers}")
numbers.sort() # 升序排序
print(f"sort() 升序後： {numbers}")

numbers.sort(reverse=True) # 降序排序
print(f"sort() 降序後： {numbers}")

# 注意： sorted() 函式 (非方法) 會回傳一個新的排序好的列表，不修改原始列表
unsorted_numbers = [50, 20, 80, 10]
sorted_numbers = sorted(unsorted_numbers)
print(f"使用 sorted() 排序後： {sorted_numbers}")
print(f"原始列表 (未修改)： {unsorted_numbers}")

# 4. 反轉列表 (reverse()) 
# reverse() 方法會「直接修改」原始列表，將其元素順序反轉。
my_values = ["A", "B", "C", "D"]
print(f"\n原始列表 (反轉範例)： {my_values}")
my_values.reverse()
print(f"reverse() 後： {my_values}")

# 5. 複製列表 (copy()) 
# 直接使用 '=' 賦值會導致兩個變數指向同一個列表。 
# 使用 copy() 方法會創建一個獨立的副本。

original_list = [10, 20, 30]
# 錯誤的複製方式 (兩者會互相影響) 
# alias_list = original_list 
# alias_list.append(40) 
# print(f"原始列表 (錯誤複製影響): {original_list}")

# 正確的複製方式
copied_list = original_list.copy()
copied_list.append(40)
print(f"\n原始列表 (copy() 後)： {original_list}") # original_list 不受影響
print(f"複製列表 (copy() 後)： {copied_list}")

# 6. 清空列表 (clear()) 
# clear() 方法會移除列表中的所有元素，使其變成空列表。
temp_list = ["one", "two", "three"]
print(f"\n清空前： {temp_list}")
temp_list.clear()
print(f"清空後： {temp_list}")

# --- 元組 (Tuples) - 創建範例 --- 
print("\n--- 元組 (Tuples) - 創建範例 ---")

# 創建一個包含數字的元組
coordinates = (10, 20)
print(f"座標元組： {coordinates}")
print(f"型別：{type(coordinates)}")

# 創建一個包含不同資料型別的元組
person_info = ("Bob", 30, False)
print(f"個人資料元組： {person_info}")

# 創建一個空元組
empty_tuple = ()
print(f"空元組： {empty_tuple}")

# --- 元組 (Tuples) - 單一元素與存取範例 --- +
print("\n--- 元組 (Tuples) - 單一元素與存取範例 ---")
# 1. 創建單一元素的元組 (注意逗號是必須的！) 
# 有逗號，這才是元組
single_element_tuple = ("hello",)
print(f"單一元素的元組： {single_element_tuple}")
print(f"型別 (有逗號)： {type(single_element_tuple)}")

# 沒有逗號，這不是元組，只是一個字串
not_a_tuple = ("hello")
print(f"沒有逗號的單一元素： {not_a_tuple}")
print(f"型別 (沒逗號)： {type(not_a_tuple)}")

# 2. 存取元組元素 (和列表一樣，使用索引) 
# 使用之前創建的 coordinates = (10, 20) 和 person_info = ("Bob", 30, False)
print(f"\n從座標元組 {coordinates} 存取：")
print(f"X 值 (索引 0)： {coordinates[0]}") # 存取第一個元素

print(f"\n從個人資訊元組 {person_info} 存取：")
print(f"名字 (索引 0)： {person_info[0]}")
print(f"是否是學生 (索引 2)： {person_info[2]}")
print(f"最後一個元素 (索引 -1)： {person_info[-1]}")
print(f"倒數第二個元素 (索引 -2)： {person_info[-2]}")

# 執行下面這行程式碼會報錯，因為元組不可變！ 
# 請不要解除註解並執行它，僅為演示其不可變特性。 
# coordinates[0] = 30 # 這行會報錯：TypeError: 'tuple' object does not support item assignment 
# print(f"嘗試修改元組後: {coordinates}")

# --- 元組 (Tuples) - 其他操作範例 --- 
print("\n--- 元組 (Tuples) - 其他操作範例 ---")

my_tuple = (1, 2, 3, 4, 5) 
another_tuple = (6, 7, 8)

# 1. 檢查元素是否存在 (in 關鍵字)
print(f"原始元組： {my_tuple}")
print(f"2 是否在 my_tuple 中？ {2 in my_tuple}")
print(f"10 是否在 my_tuple 中？ {10 in my_tuple}")

# 2. 獲取元組長度 (len() 函式)
print(f"my_tuple 的長度： {len(my_tuple)}")

# 3. 元組的連接 (+) 
# 會創建一個新的元組
combined_tuple = my_tuple + another_tuple
print(f"連接後的元組： {combined_tuple}")
print(f"原始 my_tuple 是否改變？ {my_tuple}") # 沒有改變

# 4. 元組的重複 (*) 
# 會創建一個重複元素的新元組
repeated_tuple = ("hello",) * 3
print(f"重複後的元組： {repeated_tuple}")

# 5. 元組解包 (Tuple Unpacking) - 非常有用！ 
# 如果知道元組的元素數量，可以直接將它們賦值給多個變數。
coordinates_tuple = (100, 200)
x, y = coordinates_tuple # 將元組的元素分別賦值給 x 和 y
print(f"\n解包座標：x = {x}, y = {y}")

# 常見應用：交換變數的值 (不需中間變數)
a = 5
b = 10
print(f"交換前： a = {a}, b = {b}")
a, b = b, a # Python 的魔法！右邊會先創建一個臨時的元組 (10, 5)
print(f"交換後： a = {a}, b = {b}")

# --- 字典 (Dictionaries) - 創建與存取範例 --- 
print("\n--- 字典 (Dictionaries) - 創建與存取範例 ---") 

# 1. 創建字典 
# 創建一個表示個人資訊的字典
person = {
	"name": "Sean",
	"age": 30,
	"city": "Taipei",
	"is_student": False
}
print(f"個人資訊字典：{person}")
print(f"型別： {type(person)}")

# 創建一個空字典
empty_dict = {}
print(f"空字典： {empty_dict}")

# 2. 存取字典的值 (透過鍵)
print(f"\n存取字典元素：")
print(f"姓名： {person['name']}") # 訪問 'name' 鍵對應的值
print(f"年齡： {person['age']}") # 訪問 'age' 鍵對應的值
print(f"城市： {person['city']}") # 訪問 'city' 鍵對應的值

# 如果嘗試存取不存在的鍵，會報錯 (KeyError) 
# print(person['country']) # 解除註解會報錯：KeyError: 'country'

# --- 字典 (Dictionaries) - 常見操作範例 --- 
print("\n--- 字典 (Dictionaries) - 常見操作範例 ---") 
# 使用之前創建的個人資訊字典 
# person = {"name": "Sean", "age": 30, "city": "Taipei", "is_student": False}
print(f"原始字典： {person}")

# 1. 新增/修改鍵值對 
# 新增一個新的鍵值對
person["occupation"] = "Data Scientist"
print(f"新增 'occupation' 後： {person}")

# 修改已存在的鍵的值
person["age"] = 31
print(f"修改 'age' 後： {person}")

# 2. 刪除鍵值對 
# 使用 del 語句刪除
del person["is_student"]
print(f"del 'is_student' 後： {person}")

# 使用 pop() 方法刪除並回傳值
removed_city = person.pop("city")
print(f"pop 'city' 後： {person}")
print(f"被 pop 掉的城市： {removed_city}")

# 3. 檢查鍵是否存在 (in 關鍵字)
print(f"\n'name' 是否在字典中？ {'name' in person}")
print(f"'city' 是否在字典中？ {'city' in person}")

# 4. 獲取所有鍵/值/鍵值對
print(f"\n所有鍵：{person.keys()}")
print(f"所有值： {person.values()}")
print(f"所有鍵值對： {person.items()}")

# 可以將這些視圖轉換成列表，以便於查看和進一步操作
print(f"所有鍵 (列表形式)： {list(person.keys())}")
print(f"所有值 (列表形式)： {list(person.values())}")