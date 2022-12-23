# Two number sum.
# Variable, Condition Control, Loop, Function

'''
list
numbers = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
从小到大排序
numbers.sort()

在 numbers 尝试找到两个数字相加的和 等于 targetSum
如果有的话，就返回这两个数字
如果没有，就返回 -1, -1
'''

numbers = [3, 5, -4, 8, 11, 1, 6]
'''
print(numbers)
print(numbers[1]) # 访问列表中元素的方法：列表名[位置]
print(len(numbers)) # len - 得到列表中元素的个数
print(numbers[len(numbers) - 1]) # 最后一个元素的位置 len(列表名) - 1
'''

numbers.sort()
targetSum = 10
#                            r = 3
# numbers = [-4, -1, 1, 3, 5, 6, 8, 11]
#                l = 3
# targetSum = 10
# 设置左右标记
l = 0
r = len(numbers) - 1

'''
把左右两个位置上的数字相加
如果和小了，就把 l 往右移动一位
如果和大了，就把 r 往左移动一位
如果和等于targetSum，就直接结束并打印结果

不断重复上面的过程，直到 l == r 为止，如果 l == r，说明不存在两个数字相加可以等于 targetSum
'''
while l < r:
    s = numbers[l] + numbers[r]

    if s < targetSum:
        l = l + 1
    elif s > targetSum:
        r = r - 1
    else: # s == targetSum
        break # 打断 while 循环，不再继续

# 第一轮：-4 + 8 = 4
# s = numbers[l] + numbers[r]

# 如果 s > targetSum，说明什么？
# 两个加数太大了 -> 尝试减小这两个加数 -> r 标记向左移动一个位置

# 如果 s < targetSum，说明什么？
# 两个加数太小了 -> 尝试增大两个加数 ->

# 如果 s == targetSum，说明找到匹配了
if l == r:
    print("不存在这样的两个数字")
else:
    print(numbers[l])
    print(numbers[r])










