# -*- coding: UTF-8 -*-
__author__ = 'luoxiao_y'


# list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print list[:5:2]

# f = open('1.txt', 'w')
# t = ['no no \n', 'oh no \n']
# try:
#     f.writelines(t)
# # finally:
# #     f.close()
#
# import os
#
# fd =open('2.txt', os.O_CREAT | os.O_RDWR)
#
# print '你好，世界'
#
# list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# list.append(10)
# print list
# list.insert(15, 1)
# print list
# del(list[2])
# print list
# y = ['a', 'b', 'c']
# x = y
# x[1] = 'z'
# print x
# print y
#
# m = ['a', 'b', 'c']
# n = m[:]
# n[1] = 'z'
# print n
# print m

# y = ['z', 'x', 'c']
# x = y
# x = ['a', 'b', 'c']
# print x
# print y

# class Person(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.__gender = gender
#
#     def get_gender(self):
#         return self.__gender
#
#
# class Student(Person):
#     def __init__(self, name, gender, grade):
#         super(Student, self).__init__(name, gender)
#         self.grade = grade
#
#     def cmp(self, s):
#         if self.grade > s.grade:
#             return 'you are greater than %s' %(self.name)
#         return 'no greater'
#
# if __name__ == '__main__':
#     a = Student('Alien', 'Male', 95)
#     b = Student('En', 'Female', 85)
#     print a.cmp(b)
#
# import numpy
#
# a = [11.2, 12.36, 13.56, 15.22, 11.68, 12.56]
# no = numpy.array(a)
# print no
# print no > 15
# print no[no > 15]
# print no[no < 15]

import numpy as np

# height = np.round(np.random.normal(1.75, 0.20, 5000), 2)
# weight = np.round(np.random.normal(60.32, 15, 5000), 2)
# np_school = np.column_stack((height, weight))
# # print np_school
# print np.mean(np_school[:, 0])
# print np.median(np_school[:, 1])
# print np.corrcoef(np_school[:, 0], np_school[:, 1])

# t = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
# bsis = np.array(t)
# print type(bsis)
# print bsis

# import matplotlib.pyplot as plt
# year = [1950, 1970, 1990, 2010]
# pop = [2.519, 3.692, 5.263, 6.972]
# year = [1800, 1850, 1900]+year
# pop = [1.0, 1.262, 1.650]+pop
# plt.fill_between(year, pop, 0, color='blue')
# plt.plot(year, pop)
# plt.xlabel("Year")
# plt.ylabel('Num')
# plt.title('The World People')
# plt.yticks([0, 2, 4, 6, 8, 10, 12], ['0B', '2B', '4B', '6B', '8B', '10B', '12B'])
# plt.show()
# plt.scatter(year, pop)
# plt.show()
#

# sample = [1.2, 2.3, 5.8, 1.5, 2.6, 3.8, 2.4, 6.5, 7.5, 7.8]
# plt.hist(sample, bins=5)
# plt.show()