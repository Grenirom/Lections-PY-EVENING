"===============================Set================================="
# Множество(set) -изменяемый, неупорядоченный, итерируемый, неиндексируемый тип данных, предназначенный для хранния уникальных значений. Множество могут хранить в себе только не изменяемый типы данных


set1 = {1, 2, 3, 4}
set2 = {1, 2, 1, 2, 3, 1, 2, 4, 1, 1, 1}
print(set2)# {1, 2, 3, 4}

set3 = {(1, 2, 3), 1, 2, 3}
print(set3)# {1, 2, 3, (1, 2, 3)}
set4 = {1, 2, 1, 1, True, False, 0}
print(set4)# {False, 1, 2}
"============================FIFO/ LIFO============================="
# FIFO - First in first out
# LIFO - last in first out


"============================Методы set============================="
# print(dir(set2))

# add() - длбавляет элементы в set
set1 = {1, 2, 3, 4, 5}
set1.add(None)
set1.add(10)
set1.add(1) 
print(set1)# {None, 1, 2, 3, 4, 5, 10}

#pop() - удаляет и возвращает случайный элемент из set (Но есть принцип FIFO)

set1 = {1, 2, 3}
popped = set1.pop()
set1.pop()
print(set1, popped)

# remove - удаляет элемент из set по значению, если указанного элемента нет в set, то вызывается ошибка

set3 = {1, 2, 3}
set3.remove(2)
set3.remove(3)
# set3.remove(5)KeyError
print(set3)

# difference() (-) - находит отличие вв двух множествах
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.difference(set2))#{1, 2}
print(set1 - set2)#{1, 2}

# symmetric_defference() - возвращает элементы уникальны для друг друга (set1) и (set2)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.symmetric_difference(set2))


# intersection() - (&) - находит пересчение в двух множествах
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set2 = {6, 7, 8, 9, 10, 11, 12}
print(set1.intersection(set2))# {8, 9, 6, 7}
# print(set1 & set2)# {8, 9, 6, 7}

print(dir(set1))
