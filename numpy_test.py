import numpy as np
import pandas as pd

a = np.array([1,3,5,7,9,11])
print('a result is :',a)

b = np.arange(1, 12, 2)    
print('b result is :',b)

c = np.linspace(5, 8, 13)
print('c result is :',c)    

d = np.zeros((4, 2))
print('d result is :',d)        

e = np.ones((2, 3), dtype=np.int16)
print('e result is :',e)

f = np.full((6,), 88)
print('f result is :',f)

g = np.fromstring('25 30 35 40', dtype=np.int, sep=' ')
print('g result is :',g)

h = np.array([[1,3,5],[7,9,11]])
print('h result is :',g)

i = np.zeros_like(a)    
print('i result is :',i)

import numpy as np
student = np.dtype([('name','S20'),('age','i1'),('mark','f4')])
a= np.array([('abc',21,50),('xyz',18,75)],dtype=student)
print (a)

#[(b'abc', 21, 50.) (b'xyz', 18, 75.)]


import numpy as np          #seting the shape and rearrangeing the shape of the matrices
a= np.array([[1,2,3],[4,5,6]])
#a.shape=(3,2)
print(a.shape)


import numpy as np
a = np.arange(25)
b = a.reshape(5,5)
print(b)


import numpy as np
a = np.zeros((2,2),dtype = [('x','i4'),('y','i4')])
print(a)

import numpy as pd 
x=[1,1,2]
a=np.asarray(x,dtype=float)
print(a)

import numpy as np
x=[1,2,3]
a=np.asarray(x)
print(a)

import numpy as np 
list = np.arange(5) 
print (list)

import numpy as np
a = np.arange(20)
b = slice(2,20,2) 
print(a[b])

import numpy as np
a = np.arange(20)
b = a[2:20:2]
print(b)

import numpy as np
a = np.arange(20)
b = a[5:12]
print(b)


import numpy as np
a = np.arange(0,60,5)
a = a.reshape(3,4)
print ('Original array is:','\n')

print (a)

print ('Modified array is:')
for x in np.nditer(a):
   print (x)


import numpy as np
a = np.arange(0,60,5)
a = a.reshape(3,4)
print ('Original array is:')
print (a)
print ('\n')

print ('Transpose of the original array is:')
b = a.T
print (b)
print ('\n')

print ('Sorted in C-style order:')
c = b.copy(order = 'C')
print (c)
for x in np.nditer(c):
    print (x)

print ('\n')

print ('Sorted in F-style order:')
c = b.copy(order = 'F')
print (c)
for x in np.nditer(c):
    print (x)


import numpy as np
a = np.arange(0,60,5)
b = a.reshape(3,4)
print(b)
for x in np.nditer(b,op_flags=['readwrite']):
    x[...]=2*x
print(b)
print("modified array is :")

print("sorted in C-shape style:")
for x in np.nditer(a,order='C'):
    print(x)

print("sorted in F-shape style:")
for x in np.nditer(a,order='F'):
    print(x)

class Shape:
	def __init__(self, color=None):
		self.color = color
		
	def get_color(self):
		return self.color
		
	def __str__(self):
		return self.get_color() + ' Shape'
		
class Rectangle(Shape):
	def __init__(self, color, length, width):
		super().__init__(color)
		self.length = length
		self.width = width
		
	def get_area(self):
		return self.length * self.width
		
	def get_perimeter(self):
		return 2 * (self.length + self.width)
		
	def __str__(self):
		return self.get_color() + ' ' + str(self.length) + 'x' + str(self.width) + ' ' + type(self).__name__

from math import pi		
class Circle(Shape):
	def __init__(self, color, radius):
		super().__init__(color)
		self.radius = radius
		
	def get_area(self):
		return pi * self.radius ** 2
		
	def get_perimeter(self):
		return 2 * pi * self.radius
		
def print_shape_data(self):
	print('Shape:    ', type(self).__name__)
	print('Color:    ', self.get_color())
	print('Area:     ', self.get_area())
	print('Perimeter:', self.get_perimeter())
	
shape = Shape('red')
print('shape is', shape.get_color())

rect = Rectangle('blue', 6, 4)
print('rect is', rect.get_color(), ' with area:', rect.get_area(), ' and perimeter:', rect.get_perimeter())

circ = Circle('green', 5)
print('circ is', circ.get_color(), ' with area:', circ.get_area(), ' and perimeter:', circ.get_perimeter())

print('rect is a', type(rect).__name__)
print('circ is a', type(circ).__name__, '\n')

	
my_new_shape = Rectangle('yellow', 17, 9)
print_shape_data(my_new_shape)

print(type(my_new_shape))
print(my_new_shape)