#Сортировка выбором

def smallest(l):
   """Функция для поиска самого маленького значения в списке"""
   small = l[0]
   smallIndex = 0
   for i in range(1, len(l)):
      if l[i] < small:
         small = l[i]
         smallIndex = i
   return smallIndex

def sort(l):
   """Функция сортировки списка по возрастанию"""
   newL = []
   for i in range(len(l)):
      small = smallest(l)
      newL.append(l.pop(small))
   return newL 

import random

def randomL(n):
   """Функция для создания списка со случайными значениями"""
   L = []
   i = 0
   while i < n:
      m = random.randint(-100, 100)
      if m not in L:
         L.append(m)
         i += 1
   return L

L = randomL(20)
print(L)
print(sort(L))
