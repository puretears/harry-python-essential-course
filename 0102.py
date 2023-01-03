# 变量和获取输入
# 变量是用来存储各种值的
# 有哪些类型的值可以存在变量里：
# +1 / -1 / 0 - 整数 - int(eger)
# 1/2         - 浮点数
# 3.1415      - 浮点数
# "Fiona"     - 字符串
# [1, 2, 3, 4, 5] - list, 列表
#
# 真 / 假 => 布尔变量 => True / False
# 2 > 1, 1/2 等于 0.5 => True
# 1 > 2, 1/2 大于 0.5 => False
#
# （我们写的这个程序）获取（执行我们这个程序的人）输入
# input - 获取用户输入的函数
# 我们如何能得到用户的这个输入？
# name = input("Please input your name: ")

# 打印变量 name 的值
# Your name is: ?????
# f(ormat)-String: 格式字符串
# print(f"Your name is: {name}")

# 写一个程序，输入一个年份，输出这个年份是不是闰年。
year = input("Please input the year:")
# 从 input 获取到的值的类型是字符串
# 此时，我们从键盘获取的用户输入 year，这里面保存的是一个字符串。
# ** 从 input 获取到的任何输入，他的类型都是字符串。**

# 判断 year 的值是不是一个闰年
year = int(year)  # "2000" => 2000


# 判读闰年的方法？
# ** 如果年份可以被 400 整除，那么这年是个闰年 **
# % 运算符 - 计算两个数字相除的余数
# 6 % 2 = 0
# 8 % 5 = 3
# 1 除以 9 = 1 里面包含多少个 9 = 0
# 1 除以 9 商 0 余 1
# 3 除以 7 = 3 里面包含多少 7 = 0
# 3 除以 7 商 0 余 3
# 6 % 9 = 6
# 1 % 8 = 1
# 判断 year % 400 是否等于 0
#

def is_leap_year(y: int) -> bool:
    if y % 400 == 0:
        return True
    elif y % 4 == 0 and y % 100 != 0:
        return True
    else:
        return False


if is_leap_year(year):
    print(f"{year} is leap year.")
else:
    print(f"{year} is not leap year.")
