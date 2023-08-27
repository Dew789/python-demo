"""
题目：输入一个整形数组，数组里有正数也有负数。
数组中连续的一个或多个整数组成一个子数组，
每个子数组都有一个和。求所有子数组的和的最大值。
要求时间复杂度为O(n)
"""


def max_sub_array(t):
    """sum[i] = max(sum(i-1)+t[i], t[i])
    """
    curr_sum = 0
    max_sum = 0
    for num in t:
        curr_sum += num
        if curr_sum <=0:
            curr_sum = 0
        if curr_sum > max_sum:
            max_sum = curr_sum
    if max_sum == 0:
        max_sum = max(t)

    print(max_sum)


if __name__ == '__main__':
    test_case = [1, -2, 3, 10, -4, 7, 2, -5]
    max_sub_array(test_case)
