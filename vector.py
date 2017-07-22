# coding=utf-8
import math

class Vector:
    def __init__(self, pos):
        self.pos = pos

    def __add__(self, other):
        return Vector([round(a + b, 3) for a, b in zip(self.pos, other.pos)])

    def __sub__(self, other):
        return Vector([round(a - b, 3) for a, b in zip(self.pos, other.pos)])

    def __str__(self):
        return "Vector: {}".format(self.pos)

    def len(self):
        return round(math.sqrt(sum([a * a for a in self.pos])), 3)

    def __mul__(self, times):
        '''向量乘法
        
        :param times: 乘数
        :return: 
        '''
        return Vector([round(a * times, 3) for a in self.pos])

    def __div__(self, other):
        return Vector([round(a / other, 3) for a in self.pos])

    def normalize(self):
        '''向量标准化
        
        :return: 
        '''
        return self / self.len()

    def dot_product(self, other):
        

v1 = Vector([1, 2])
v2 = Vector([1, 3])

va1 = Vector([-0.221, 7.437])
va2 = Vector([5.581, -2.136])

vb1 = Vector([8.813, -1.331, -6.247])
vb2 = Vector([1.996, 3.108, -4.554])

print va1.len()
print va2.normalize()

print vb1.len()
print vb2.normalize()

print Vector()
