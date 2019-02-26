#!/usr/bin/env python
# coding:utf-8

""" enum 枚举类型 """

from enum import Enum

Animal = Enum('myAnimal', 'ANT BEE CAT DOG')    #The first argument of the call to Enum is the name of the enumeration.The second argument is the source of enumeration member names. 
Month = Enum('Month', ('Jan','Feb', 'Mar', 'Apr', 'May', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
Subject = Enum('mySubject', ('Math','Physic', 'Biology', 'Music', 'History', 'Art', 'Science', 'Geography', 'Chemistry'))
Color = Enum('myColor',('orange','red','yello','green','blue','indigo','purple','red_alias'))
class Weekday(Enum):
    Sun = 7
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

for name, member in Color.__members__.items():
    print(name, '=>', member, ',', member.value)

print('------')

print(Animal)
print(Animal.ANT)
print(Animal.ANT.value)
print(list(Animal))

print(Month.Jan)
print(Month.Jan.value)
print(Subject.Music)
print(Subject.Music.value)
print(Weekday.Tue)
print(Weekday.Tue.value)
print(Color.purple)
print(Color.purple.value)
print(myColor.purple)   # error