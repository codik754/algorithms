#Бинарный поиск

#Формируем список для поиска
L = []
for i in range(1001):L.append(i)

#Алгоритм бинарного поиска
def binarySearch(l, item):
   low = 0
   high = len(l) - 1

   while low <= high:
      mid = int((low + high) / 2)
      guess = l[mid]
      if guess == item:
         return mid
      if guess > item:
         high = mid -1
      else:
         low = mid + 1
   return None

m = int(input('Какой элемент в списке нужно найти: '))

print(binarySearch(L, m))
