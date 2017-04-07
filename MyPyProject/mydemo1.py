# coding = utf-8
# import math
# def add(x,y,f):
# return f(x)+f(y)

# print add(4,9,math.sqrt)

# def format_name(s):
# return s[0].upper()+s[1:].lower()
# print map(format_name,['adam','LISA','Allen'])

# def sum_integral(x,y):
# return x*y
# print reduce(sum_integral,[2,4,5,7,12])

# import math
# def filter_number(x):
# a=range(1,11)
# return math.sqrt(x) in a
# print filter(filter_number,range(1,100))

#
# def sc(x):
# return x*x
# def calc_prod(lst):
# def inline_calc_prod():
# return map(sc,lst)
# return inline_calc_prod
# f =calc_prod([1,2,3,4,5,6,7])
# print f()

# def sc(x,y):
# return x*y
# def calc_prod(lst):
# def inline_calc_prod():
# return reduce(sc,lst)
# return inline_calc_prod
# f =calc_prod([1,2,3,4])
# print f()

# def count():
# fs = []
# for i in range(1, 4):
# def f():
# return i*i
# fs.append(f)
# return fs

# f1=count()
# f2=count()
# print f1()
# print f2()

# def count(lst):
# def sum_inter():
# def sc(x):
# return x*x
# return map(sc,lst)
# return sum_inter
# a=range(1,4)
# f=count(a)
# print f
# print f()

# def count():
# fs = []
# for i in range(1, 4):
# def f(j):
# def g():
# return j*j
# return g
# r = f(i)
# fs.append(r)
# return fs
# f1, f2,f3= count()
# print f1(), f2(),f3()

# print filter(lambda s:s and len(s.strip())>0,['test',None,'','str','  ','END'])

# def f1(x):
# return x*2

# def f_docorate(f):
# def ff_docorate(x):
# print 'call'+f.__name__+'()'
# return f(x)
# return ff_docorate

# f = f_docorate(f1)
# print f(2)
# f1=f_docorate(f1)
# print f1(2)
# import time

# def performance(f):
# def f_performance(*args,**kw):
# t1=time.time()
# r=f(*args,**kw)
# t2=time.time()
# print 'call %s()in%fs'%(f.__name__,(t2-t1))
# return r
# return f_performance

# def performance(prefix):
# def performance_decorator(f):
# def wrapper(*args,**kw):
# if prefix =='ms':
# t1=time.time()
# r=f(*args,**kw)
# t2=time.time()
# print '%s call %s()in%f ms'%(prefix,f.__name__,(t2-t1)*1000)
# return r
# if prefix =='s':
# t1=time.time()
# r=f(*args,**kw)
# t2=time.time()
# print '%s call %s()in%f s'%(prefix,f.__name__,(t2-t1))
# return r
# return wrapper
# return performance_decorator

# @performance('ms')
# def factorial(n):
# return reduce(lambda x,y:x*y,range(1,n+1))
# print factorial(20)
# @performance('s')
# def factorial(n):
# return reduce(lambda x,y:x*y,range(1,n+1))
# print factorial(20)
# print factorial.__name__

# import time ,functools
# def performance(prefix):
# def in_performance(f):
# def wrapper(*args,**kw):
# if prefix =='ms':
# t1=time.time()
# r=f(*args,**kw)
# t2=time.time()
# print '%s call %s()in%f ms'%(prefix,f.__name__,(t2-t1)*1000)
# return r
# if prefix =='s':
# t1=time.time()
# r=f(*args,**kw)
# t2=time.time()
# print '%s call %s()in%f s'%(prefix,f.__name__,(t2-t1))
# return r
# return wrapper
# return in_performance

# @performance('ms')
# def factorial(n):
# return reduce(lambda x,y:x*y,range(1,n+1))
# print factorial(20)
# @performance('s')
# def factorial(n):
# return reduce(lambda x,y:x*y,range(1,n+1))
# print factorial(20)
# print factorial.__name__

# import functools
# sorted_ignore_case = functools.partial(sorted,cmp=lambda x,y:-cmp(x.lower(),y.lower()))
# print sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit'])

# from os import path

# print path.isdir(r'c:\windows')
# print path.isfile(r'G:\eclipse\eclipse.exe')

# try:
# from json import dumps
# except ImportError:
# from simplejson import dumps
# print dumps({'python':2.7})

# from __future__ import unicode_literals
# s='am I an unicode?'
# print isinstance (s,unicode)

# class Person(object):
# def __init__(self,name):
# self._name=name
# xiaoming=Person('xiaoming')
# xiaofang=Person('xiaofang')
# print xiaoming.__dict__
# print xiaofang.__dict__
# print xiaoming._name
# print xiaofang._name
# print xiaofang
# print xiaoming
# print xiaofang == xiaoming

# class Person(object):
# pass
# p1=Person()
# p1.name='Bart'
# p2=Person()
# p2.name='Lisa'
# p3=Person()
# p3.name='adam'
# def sort_non_big(x,y):
# t1=x.upper()
# t2=y.upper()
# if t1<t2:
# return -1
# if t1>t2:
# return 1
# return 0


# L1=[p1.name,p2.name,p3.name]
# L2=sorted(L1,sort_non_big)
# print L2


# class Person(object):
# def __init__(self,name,genda,birth,**kw):
# self.name=name
# self.genda=genda
# self.birth=birth
# for k,v in kw.iteritems():
# setattr(self,k,v)
# p1=Person('Xiao Ming','Male','1990-1-1',job='Student')
# print p1.name
# print p1.job

# class Person(object):
# def __init__(self,name,score):
# self._name=name
# self.__score=score
# p1=Person('shengxiongyu',100)
# print p1._name
# print p1._Person__score
# print p1.__dict__

# class Person(object):
# count=0
# def __init__(self):
# Person.count=Person.count+1
# p1=Person();
# p2=Person();
# print Person.count


# class Person(object):
# def inteable(self):
# print self
# print self.__class__
# p=Person()
# p.inteable()

# class Person(object):
# __count=0
# def __init__(self):
# Person.__count=Person.__count+1
# p1=Person()
# p2=Person()
# print p2._Person__count
# class Person(object):
# def __init__(self,score):
# self.__score=score
# def return_score_level(self):
# if self.__score>90 and self.__score<=100:
# return 'A'
# elif self.__score>=60 and self.__score<=90:
# return 'B'
# elif self.__score>0 and self.__score<60:
# return 'C'
# else:
# return 'Error'

# if __name__=='__main__':
# p=Person(95)
# print 'Your level is %s' %(p.return_score_level())+p.return_score_level()

# class Person(object):
# def __init__(self,name,grade):
# self.name=name
# self._grade=grade
# self.get_grade=lambda: 'A'
# p=Person('sheng',90)
# print p.get_grade
# print p.get_grade()

# class Person(object):
# count=0
# def __init__(self):
# self.count=Person.count+1
# p1=Person();
# p2=Person();
# print p2.count

# class Person(object):
# __count=0
# def __init__(self,**kw):
# for k,v in kw.iteritems():
# setattr(self,k,v)
# Person.__count=Person.__count+1
# @classmethod
# def get_count(cls):
# return cls.__count

# p1=Person(name='sheng',score=90)
# print p1.__dict__
# p2=Person(name='xiong',score=100,job='student')
# print p2.__dict__
# print Person.get_count()

# class Activity(object):
# def __init__(self,name,genda):
# self._name = name
# self.genda = genda
# def get_name(self):
# return self._name
# def get_genda(self):
# return self.genda

# class Student(Activity):
# count=0
# def __init__(self,name,genda,money):
# super(Student,self).__init__(name,genda)
# self.__money=money
# Student.count=Student.count+1
# @classmethod
# def get_count(cls):
# return cls.count
# def get_money(self):
# return self.__money

# if __name__ =='__main__':
# stu=Student('sheng','boy',100)
# print stu.get_name()
# print stu.get_genda()
# print stu.get_money()
# print Student.get_count()


# class Person(object):
# count=0
# def __init__(self,name,gender):
# self.name=name
# self.__gender=gender
# Person.count=Person.count+1
# def get_gender(self):
# return self.__gender

# class Teacher(Person):
# def __init__(self,name,gender,course):
# super(Teacher,self).__init__(name,gender)
# self.course=course
# def get_course(self):
# print Teacher.count
# return self.course
# def get_name(self):
# return self.name
# def get_gender(self):
# return self._Person__gender


# if __name__ =='__main__':
# t1=Teacher('sheng','boy','math')
# t1.get_course()
# print t1.get_course()
# print t1.get_name()
# print t1.__dict__
# print t1.get_gender()
# print t1.count
# t2=Teacher('sheng','boy','math')
# t2.get_course()
# print t2.get_course()
# print t2.get_name()
# print t2.__dict__
# print t2.get_gender()
# print t2.count

# class Person(object):
# count = 0
# def __init__(self,name,gender):
# self.name=name
# self.__gender=gender
# Person.count=Person.count+1
# def get_gender(self):
# return self.__gender
# class Student(Person):
# def __init__(self,name,gender,score):
# super(Student,self).__init__(name,gender)
# self.score=score

# class Teacher(Person):
# def __init__(self,name,gender,course):
# super(Teacher,self).__init__(name,gender)
# self.course=course

# if __name__ =='__main__':
# p=Person('sheng','boy')
# s=Student('LOL','girl',98)
# t=Teacher('wo','girl','math')
# print isinstance(t,Person)
# print isinstance(t,Teacher)
# print isinstance(t,Student)
# print t.count

# import json
# class Student(object):
# def __init__(self,name):
# self.name=name
# def read(self):
# return self.name

# s=Student( r'["Tim", "Bob", "Alice"]')
# print json.load(s)

# import json
#
#
# class Student(object):
#     def __init__(self, name):
#         self.name = name
#     def read(self):
#         return self.name
#
# if __name__ == '__main__':
#     s = Student(r'["Tim", "Bob", "Alice"]')
#     print json.load(s)
#
# import json
#
#
# class Students(object):
#     def read(self):
#         return r'["Tim", "Bob", "Alice"]'
#
# s = Students()
#
# print json.load(s)


# class Person(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.__gender = gender
#
#
# class Teacher(Person):
#     def __init__(self, name, gender, course):
#         super(Teacher, self).__init__(name, gender)
#         self.course = course
#
#
# class Student(Person):
#     def __init__(self, name, gender, score):
#         super(Student, self).__init__(name, gender)
#         self.score = score
#
#
# class SkillMixin(object):
#     pass
#
#
# class BasketballMixin(SkillMixin):
#     def skill(self):
#         return 'Basketball'
#
#
# class FootballMixin(SkillMixin):
#     def skill(self):
#         return 'Football'
#
#
# class Bsstudent(Student, BasketballMixin):
#     def __init__(self, name, gender, score):
#         super(Bsstudent, self).__init__(name, gender, score)
#
#     def get_message(self):
#         return self.name, self._Person__gender, self.score
#
#
# class Ftteacher(Teacher, FootballMixin):
#     def __init__(self, name, gender, course):
#         super(Ftteacher, self).__init__(name, gender, course)
#
#     def get_message(self):
#         return self.name, self._Person__gender, self.course
#
#
# if __name__ == '__main__':
#     bs = Bsstudent('sheng', 'boy', 98)
#     print bs.name + ' is the best ' + bs.skill() + 'people'
#     # print bs.__dict__
#     print bs.get_message()
#     for k in bs.get_message():
#         print k
#     ft = Ftteacher('yu', 'boy', 'English')
#     print ft.name + ' is the best ' + ft.skill() + 'people'
#     print ft.get_message()

# class apple(object):
#     def __init__(self, a):
#         self.a = a
#         print 'apple ...'
# class bpple(apple):
#     def __init__(self, a, b):
#         apple.__init__(self, a)
#         self.b = b
#         print 'bpple ...'
# class cpple(apple):
#     def __init__(self, a, c):
#         apple.__init__(self, a)
#         self.c = c
#         print 'cpple ...'
# class dpple(bpple, cpple):
#     def __init__(self, a, b, c, d):
#         cpple.__init__(self, a, c)
#         bpple.__init__(self, a, b)
#         self.d = d
#         print 'dpple ...'
#
# d = dpple('a', 'b', 'c', 'd')
#
# class Person(object):
#     def __init__(self, name, gender, **kw):
#         self.name = name
#         self.gender = gender
#         for k, v in kw.iteritems():
#             setattr(self, k, v)
#
# if __name__ == '__main__':
#     s = Person('Bob', 'Male', age=18, course='Python')
#     print getattr(s, 'age')
#     print getattr(s, 'course')

# class Person(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
#
#
# class Student(Person):
#     def __init__(self, name, gender):
#         super(Student, self).__init__(name, gender)
#
#     def __str__(self):
#         return 'Person : %s ,%s '%(self.name, self.gender)
#         __repr__ = __str__
#
# if __name__ == '__main__':
#     s = Student('sheng', 'Male')
#     print s
#     s
#
# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def __str__(self):
#         return ' %s : %s' % (self.name, self.score)
#
#     __repr__ = __str__
#
#     def __cmp__(self, s):
#         if self.score == s.score:
#             return cmp(self.name.upper(), s.name.upper())
#         return -cmp(self.score, s.score)
#
# L = [Student('Alice', 95), Student('bob', 80), Student('Nob', 80), Student('zon', 80)]
# print sorted(L)

# class Fib(object):
#     def __init__(self, num):
#         a = 1
#         b = 1
#         l = []
#         for i in range(num):
#             l.append(a)
#             t = a
#             a = b
#             b = t + a
#         self.num = l
#
#     def __str__(self):
#         return '%s' % self.num
#     __repr__ = __str__
#
#     def __len__(self):
#         return len(self.num)
#
# if __name__ == '__main__':
#     fb = Fib(10)
#     print fb
#     print len(fb)
#
# class Rational(object):
#     def __init__(self, p, q):
#         self.p = p
#         self.q = q
#
#     def __str__(self):
#         return '%s/%s' % (self.p, self.q)
#     __repr__ = __str__
#
#     def __add__(self, s):
#         return Rational(self.p * s.q + self.q * s.p, self.q * s.q)
#
#     def __sub__(self, s):
#         return Rational(self.p * s.q - self.q * s.p, self.q * s.q)
#
#     def __mul__(self, s):
#         return Rational(self.p * s.p, self.q * s.q)
#
#     def __div__(self, s):
#         return Rational(self.p * s.q, self.q * s.p)
#
#     def __int__(self):
#         return self.p // self.q
#
#     def __float__(self):
#         return float(self.p) / self.q
#
# if __name__ == '__main__':
#     r1 = Rational(1, 2)
#     r2 = Rational(1, 3)
#     print r1 + r2
#     print r1 - r2
#     print r1 * r2
#     print float(r1 / r2)

#
# class student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.__score = score
#
#     @property
#     def score(self):
#         return self.__score
#
#     @score.setter
#     def score(self, score):
#         if score < 0 or score > 100:
#             raise ValueError('invalid score')
#         self.__score = score
#
#     @property
#     def grade(self):
#         if self.__score >= 80:
#             return 'A'
#         elif self.__score < 60:
#             return 'C'
#         return 'B'
#
# if __name__ == '__main__':
#     s = student('Bob', 59)
#     print s.grade
#     s.score = 60
#     print s.grade
#     s.score = 79
#     print s.grade
#     print s.score

#
# class Person(object):
#     __slots__ = ('name', 'gender')
#
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
#
#
# class Student(Person):
#     __slots__ = ('score',)
#
#     def __init__(self, name, gender, score):
#         super(Student, self).__init__(name, gender)
#         self.score = score
#
#     def __str__(self):
#         return '%s:%s  grade is %s' % (self.name, self.gender, self.score)
#
#     __repr__ = __str__
#
# if __name__ == '__main__':
#     s = Student('sheng', 'Male', 98)
#     s.name = 'Tim'
#     s.score = 95
#     print s

#
# class Fib(object):
#     def __str__(self):
#         return '%s' % self.num
#     __repr__ = __str__
#
#     def __len__(self):
#         return len(self.num)
#
#     def __call__(self, num):
#         a = 1
#         b = 1
#         l = []
#         for i in range(num):
#             l.append(a)
#             t = a
#             a = b
#             b = t + a
#         return l
#
#
# if __name__ == '__main__':
#     f = Fib()
#     print f(10)
#     print len(f(10))


class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender


class Student(Person):
    def __init__(self, name, gender, *args, **kw):
        super(Student, self).__init__(name, gender)
        for k in args:
            setattr(self, k, k)
        for n, v in kw.iteritems():
            setattr(self, n, v)

if __name__ == '__main__':
    s = Student('sheng', 'Male', 'LOL', job='student')
    print s.__dict__