
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 嵌套的列表的坑

names = ['关羽', '张飞', '赵云', '马超', '黄忠']
courses = ['语文', '数学', '英语']
# 录入五个学生三门课程的成绩

# 错误 - 参考http://pythontutor.com/visualize.html#mode=edit             # [[56.0, None, None], [56.0, None, None], [56.0, None, None], [56.0, None, None], [56.0, None, None]]
# scores = [[None] * len(courses)] * len(names)                         # 初始化一个list  
# 正确                                                                  
scores = [[None] * len(courses) for _ in range(len(names))]             # 按照习惯，有时候单个独立下划线是用作一个名字，来表示某个变量是临时的或无关紧要的。
                                                                        # [[93.0, None, None], [None, None, None], [None, None, None], [None, None, None], [None, None, None]]
for row, name in enumerate(names):
    for col, course in enumerate(courses):
        scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))
        print(scores)