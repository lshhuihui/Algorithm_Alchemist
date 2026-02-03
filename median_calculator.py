"""
中位数计算器

中位数（Median）是统计学中的一个重要概念，表示一组数据按大小顺序排列后，位于中间位置的数值。
"""

def calculate_median(data):
    """
    计算一组数据的中位数
    
    参数:
        data: 数值列表，可以包含整数或浮点数
        
    返回:
        float: 中位数
        
    异常:
        ValueError: 如果输入数据为空
    """
    if not data:
        raise ValueError("输入数据不能为空")
    
    # 对数据进行排序
    sorted_data = sorted(data)
    n = len(sorted_data)
    
    # 计算中位数
    if n % 2 == 1:  # 奇数个数据
        median = sorted_data[n // 2]
    else:  # 偶数个数据
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        median = (mid1 + mid2) / 2
    
    return median


def calculate_median_with_details(data):
    """
    计算中位数并返回详细的计算过程
    
    参数:
        data: 数值列表
        
    返回:
        dict: 包含中位数和计算过程的字典
    """
    if not data:
        raise ValueError("输入数据不能为空")
    
    # 原始数据
    original_data = data.copy()
    
    # 排序后的数据
    sorted_data = sorted(data)
    n = len(sorted_data)
    
    # 计算中位数
    if n % 2 == 1:
        median = sorted_data[n // 2]
        calculation_process = f"数据个数为奇数({n})，中位数是第{n//2 + 1}个数据"
    else:
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        median = (mid1 + mid2) / 2
        calculation_process = f"数据个数为偶数({n})，中位数是第{n//2}个和第{n//2 + 1}个数据的平均值: ({mid1} + {mid2}) / 2 = {median}"
    
    return {
        '原始数据': original_data,
        '排序后数据': sorted_data,
        '数据个数': n,
        '中位数': median,
        '计算过程': calculation_process
    }


def compare_mean_median(data):
    """
    比较平均数和中位数，展示两者的差异
    
    参数:
        data: 数值列表
        
    返回:
        dict: 包含平均数、中位数和比较结果的字典
    """
    if not data:
        raise ValueError("输入数据不能为空")
    
    median = calculate_median(data)
    mean = sum(data) / len(data)
    
    difference = abs(mean - median)
    
    return {
        '平均数': mean,
        '中位数': median,
        '差异': difference,
        '分析': "平均数受极端值影响较大，中位数更能反映数据的典型水平" if difference > mean * 0.1 else "平均数和中位数相近，数据分布较均匀"
    }


# 示例和测试
def main():
    """主函数：演示中位数的计算"""
    
    print("=" * 60)
    print("中位数计算器演示")
    print("=" * 60)
    
    # 示例1：奇数个数据
    data1 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print("\n示例1 - 奇数个数据:")
    print(f"数据: {data1}")
    result1 = calculate_median_with_details(data1)
    print(f"排序后: {result1['排序后数据']}")
    print(f"计算过程: {result1['计算过程']}")
    print(f"中位数: {result1['中位数']}")
    
    # 示例2：偶数个数据
    data2 = [3, 1, 4, 1, 5, 9, 2, 6]
    print("\n示例2 - 偶数个数据:")
    print(f"数据: {data2}")
    result2 = calculate_median_with_details(data2)
    print(f"排序后: {result2['排序后数据']}")
    print(f"计算过程: {result2['计算过程']}")
    print(f"中位数: {result2['中位数']}")
    
    # 示例3：包含极端值的数据
    data3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]  # 100是极端值
    print("\n示例3 - 包含极端值的数据:")
    print(f"数据: {data3}")
    comparison = compare_mean_median(data3)
    print(f"平均数: {comparison['平均数']:.2f}")
    print(f"中位数: {comparison['中位数']}")
    print(f"分析: {comparison['分析']}")
    
    # 示例4：浮点数数据
    data4 = [3.5, 1.2, 4.8, 2.1, 5.6]
    print("\n示例4 - 浮点数数据:")
    print(f"数据: {data4}")
    median4 = calculate_median(data4)
    print(f"中位数: {median4}")
    
    print("\n" + "=" * 60)
    print("中位数计算完成！")
    print("=" * 60)


if __name__ == "__main__":
    main()