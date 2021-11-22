#Алгоритм быстрой сортировки
import random

def quicksort(l):
   """Функция, реализующая алгоритм быстрой сортировки"""
   if len(l) < 2:
      return l
   else:
      pivot = l[0]
      less = [i for i in l[1:] if i <= pivot]
      greater = [i for i in l[1:] if i > pivot]
      return quicksort(less) + [pivot] + quicksort(greater) 

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
L = quicksort(L)
print(L)
