#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 生成式（推导式）可以用来生成列表，集合和字典
# 列表生成式即List Comprehensions


nn = range(1,11)
mm = [x * x for x in nn]    # 创建一个新的list
print(mm)



prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
# 用股票价格大于100元的股票构造一个新的字典 key: value 
prices2 = {key: value for key, value in prices.items() if value > 100}  # 字典 .items() 方法返回字典键-值对
# 或者将 键 值 反转
prices3 = {value: key for key, value in prices.items() if value > 100}  # for 循环同时使用两个甚至多个变量，比如dict的iteritems()可以同时迭代key和value


print(prices2)

print(prices3)