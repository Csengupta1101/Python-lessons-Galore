# -*- coding: utf-8 -*-
"""List Comprehension.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CGbXp0Vk8H7SiOK37LiDOy_x9TJ3rMGD
"""

#List Comprehension

List1 = [56,97,51,13,58,713,22,34]
Even_List = [i for i in List1 if i%2 == 0]
Odd_List = [i for i in List1 if i%2 == 1]
print(Even_List)
print(Odd_List)
