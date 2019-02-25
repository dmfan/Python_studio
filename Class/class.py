#!/usr/bin/env python3
# coding:utf-8

""" 实例属性和类属性 """

class Student(object):
    position = 'A'
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 91
print(s.name)
print(s.score)
print(s.position)
print(Student.position)
Student.position = 'C'
print(s.position)
print(Student.position)
s.position ='D'
print(s.position)
print(Student.position)