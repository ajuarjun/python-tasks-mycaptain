# -*- coding: utf-8 -*-
"""task10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YUsijUEeWNbq6Tkz3GD8_e-WKKUHzGqI
"""

class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width

newRectangle = Rectangle(12, 10)
print("\n The area of rectangle is",newRectangle.rectangle_area())