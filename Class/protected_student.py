#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 包含私有变量的类
# 属性的名称前加上两个下划线__，表示私有属性

class Student(object):      # (object)，表示该类是从哪个类继承下来的

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'


bart = Student('Bart Simpson', 59)              # 创建实例
print('bart.get_name() =', bart.get_name())
bart.set_score(60)
print('bart.get_score() =', bart.get_score())

print('DO NOT use bart._Student__name:', bart._Student__name)   # 虽然可以通过这种方式来访问__name变量，但是不建议这么做