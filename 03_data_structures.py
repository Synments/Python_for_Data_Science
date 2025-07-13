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