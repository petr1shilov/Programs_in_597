# word = input()

# num1 = num2 = 0 
# for i in range(0, 6, 2):
#     num1 += int(word[i])

# for j in range(1, 6, 2):
#     num2 += int(word[j])

# if num1 == num2:
#     print('luck')
# else:
#     print(num1, num2)

# name = set()
# aminal = {'cat', 5, 'dog', 7, 'fox', 10, 'cat'}

# print(aminal)
# print(aminal)
# print(len(aminal))

# for i in aminal:
#     print(i)

# if 'dog' in aminal:
#     print('Elem in set')


# new_elem = 'EEEE'

# aminal.add()

# print(aminal)

# my_set = set()

# my_set.add('a')
# my_set.add('b')
# my_set.add('c')

# print(my_set)

# # my_set.remove('a')
# # print(my_set)
# # my_set.discard('a')
# # print(my_set)
# # my_set.remove('a')
# # my_set.clear()

# my_set1 = {1, 2, 3}
# my_set2 = {3, 4, 5}
# my_set3 = {3, 6, 7}

# union = my_set1.union(my_set2)
# union_1 = my_set1 | my_set2 | my_set3
# #############
# interp = my_set1.intersection(my_set2, my_set3)
# interp_1 = my_set1 & my_set2 & my_set3
# ############################
# differ = my_set1.difference(my_set2)
# differ_1 = my_set1 - my_set2
# ##########################
# sim = my_set1.symmetric_difference(my_set2)
# sim_1 = my_set1 ^ my_set2


# if my_set1 == my_set2:
#     print('Равны')


# primer = [] 
# primer.append(12)
# primer.append(114)
# primer.append(125)
# primer.append('512')


# primer_01 = [2, 4, 6]

# string_of_smth ='123'
# primer.extend(string_of_smth)

# print(primer)

# set_of_smth = {'a', 'b', 'c'}

# primer.extend(set_of_smth)

# print(primer)

# primer[3] = 1234654

# print(primer)

# primer += [32,21]
# print(primer)

# list_of = []
# num = 10 
# for i in range(10):
#     string = input()
#     list_of.append(string)

# print(primer[1: 3])

# del primer[::2]

# print(primer)
# num = primer.pop(1)
# print(num)
# print(primer)


# primer.remove(21)
# print(primer)

# primer.insert(2, 1001)

# print(primer)

# primer.sort()
# print(primer)

# # new_list = primer.copy()

# list_01 = []

# for i in range(4):
#     suma = input()
#     list_01.append(suma)

# # for j in list_01:
# #     print(j, end=',')
# word = 'kot'
# for j in list_01:
#     if word in j:
#         print(j)  
  

# tuple_one = (18,)
# tuple_two = tuple()
# print(tuple_one)
# print(tuple_one[0])

# print(type(tuple_one))

# data = input()
# print(data, type(data))
# data = data.split('.,')
# print(data, type(data))
    
# print(type(data[1]))
# num = int(data[1])

# a = [0, 3, 5, 7, 2, 1, 4, 9, 6, 8]

# for i in range(len(a) - 1):
#     for j in range(len(a) - 1 - i):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
 
# # print(a)

# print(dir([]))
# help([].sort)

name = 'Dima'
age = 16
print(f'Меня зовут {name}. Мне {age} лет')

list_age = [12, 16, 18]
x = 10
y = 20
print(f'new summ is {x} + {y} = {x + y}')

word = ' мало Средне МНОГО '

print(word.lower().strip().replace('о','ф'))
print(word)

# print(f'Диме {list_age[1]}, а Ладе {list_age[2]}')

