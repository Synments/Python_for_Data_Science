# 專案二：基礎統計分析工具 
import collections # 引入 collections 模組，用於計算眾數 
def get_numbers(): 
    """ 
    引導使用者輸入數字，並將有效數字存入列表中。 
    遇到無效輸入會提示錯誤，遇到 'q' 則結束輸入。 
    Returns: 
        list: 包含使用者輸入的數字列表。 
    """ 
    print("--- 歡迎使用基礎統計分析工具！ ---") 
    print("請輸入一組數字，每輸入一個數字後請按 Enter。") 
    print("當您輸入完所有數字後，請輸入 'q' 結束輸入。") 
    
    numbers = [] # 初始化一個空的列表 
    while True: 
        user_input = input("請輸入數字 (或輸入 'q' 結束): ") 
        if user_input.lower() == 'q': 
            break 
        try: 
            number = float(user_input) 
            numbers.append(number) 
        except ValueError: 
            print("無效輸入，請輸入有效的數字或 'q' 結束。") 
    return numbers # <-- 這行 return 必須在 get_numbers() 函式內部，且縮排正確 

def calculate_statistics(numbers_list): # 函式接收一個數字列表作為參數 
    """ 
    計算給定數字列表的基礎統計量。 
    Args: 
        numbers_list (list): 包含數字的列表。 
    Returns: 
        dict: 包含所有計算結果的字典。 
    """ 
    stats = {} # 用字典儲存所有統計結果 
    
    # 數字個數 
    stats['count'] = len(numbers_list) 
    
    # 總和 
    stats['total'] = sum(numbers_list) 
    
    # 平均值 
    stats['mean'] = stats['total'] / stats['count'] 
    
    # 最大值 
    stats['maximum'] = max(numbers_list) 
    
    # 最小值 
    stats['minimum'] = min(numbers_list) 
    
    # 中位數 
    sorted_numbers = sorted(numbers_list) 
    middle_index = stats['count'] // 2 
    
    if stats['count'] % 2 == 0: 
        stats['median'] = (sorted_numbers[middle_index - 1] + sorted_numbers[middle_index]) / 2 
    else: 
        stats['median'] = sorted_numbers[middle_index] 
    
    # 眾數 (Mode) 
    data_counts = collections.Counter(numbers_list) 
    max_freq = max(data_counts.values()) 
    modes_list = [num for num, freq in data_counts.items() if freq == max_freq] 
    
    if len(modes_list) == len(numbers_list) and max_freq == 1: 
        stats['mode'] = "無眾數 (所有數字出現次數相同)" 
    else: 
        stats['mode'] = ", ".join(map(str, sorted(modes_list))) 
    
    return stats # 返回包含所有統計結果的字典 
    
def display_results(stats_data): 
    """ 
    顯示所有計算出的統計結果。 
    Args: 
        stats_data (dict): 包含統計結果的字典。 
    """ 
    print("\n--- 統計分析結果 ---") 
    print(f"總共有 {stats_data['count']} 個數字") 
    print(f"數字總和： {stats_data['total']:.2f}") 
    print(f"平均值： {stats_data['mean']:.2f}") 
    print(f"中位數： {stats_data['median']:.2f}") 
    print(f"最大值： {stats_data['maximum']:.2f}") 
    print(f"最小值： {stats_data['minimum']:.2f}") 
    print(f"眾數： {stats_data['mode']}") 

def main(): 
    """ 主程式函式，協調整個統計分析工具的運行流程。 """ 
    numbers = get_numbers() # 呼叫函式來獲取數字 
    
    if not numbers: 
        print("錯誤：您沒有輸入任何數字，無法進行統計分析。程式將結束。") 
    else: 
        print("\n您已輸入以下數字：", numbers) 
        # 呼叫函式來計算統計量 
        statistics_results = calculate_statistics(numbers) 
        # 呼叫函式來顯示結果 
        display_results(statistics_results) 

# 程式的入口點：當檔案直接運行時，會呼叫 main() 函式 
if __name__ == "__main__": 
    main()