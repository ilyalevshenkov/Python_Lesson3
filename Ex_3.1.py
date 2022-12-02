# Задача 3 . Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.

from random import random, randrange

def GetFractionalPart(flt):
    intgr = round(flt)
    result = flt - intgr
    return result

QUANTITY = 10 
user_list = [random() * randrange(-10,10) for i in range(QUANTITY)]
print(["{:0.2f}".format(x) for x in user_list])
partitioned_user_list = list(map(lambda x: x % 1, user_list))
difference = max(partitioned_user_list) - min(partitioned_user_list)
print("{:0.2f}".format(difference))