"""实验一演示程序：计算一组数字的平均值和中位数。

用于练习 Git 的 add / commit / push 流程。
运行方法：python code/demo.py
"""


def mean_median(nums):
    """返回列表 nums 的平均值和中位数。"""
    nums = sorted(nums)
    n = len(nums)
    mean = sum(nums) / n
    if n % 2 == 1:
        median = nums[n // 2]
    else:
        median = (nums[n // 2 - 1] + nums[n // 2]) / 2
    return mean, median


if __name__ == "__main__":
    data = [1, 3, 5, 7, 9, 11]
    mean, median = mean_median(data)
    print(f"数据: {data}")
    print(f"平均值: {mean}")
    print(f"中位数: {median}")
