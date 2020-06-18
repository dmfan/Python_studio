#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 数据结构和算法2







"""
贪婪法：在对问题求解时，总是做出在当前看来是最好的选择，不追求最优解，快速找到满意解。
输入：
20 6
电脑 200 20
收音机 20 4
钟 175 10
花瓶 50 2
书 10 1
油画 90 9
"""
class Thing(object):
    """物品"""

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    @property                           # @property装饰器 可以将一个类方法变成属性让对对象调用
    def value(self):
        """价格重量比"""
        return self.price / self.weight


def input_thing():
    """输入物品信息"""
    print("输入物品--价值--重量")
    name_str, price_str, weight_str = input().split()
    return name_str, int(price_str), int(weight_str)


def main():
    """主函数"""
    print("输入小偷背包容量--户内物品种类数")
    max_weight, num_of_things = map(int, input().split())
    all_things = []
    for _ in range(num_of_things):
        all_things.append(Thing(*input_thing()))
    all_things.sort(key=lambda x: x.value, reverse=True)        # 对列表排序， 参数x取自于可迭代对象中
                                                                # 第一个参数表示 lambda匿名函数 冒号前是参数，可以有多个，用逗号隔开，冒号右边的为表达式。 表达式结果返回给key
                                                                # 第二个参数表示降序
    total_weight = 0
    total_price = 0
    for thing in all_things:
        if total_weight + thing.weight <= max_weight:
            print(f'小偷拿走了{thing.name}')
            total_weight += thing.weight
            total_price += thing.price
    print(f'总价值: {total_price}美元')


if __name__ == '__main__':
    main()
