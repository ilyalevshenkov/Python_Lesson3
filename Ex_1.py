# Задача 1 . Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12



QUANTITY = 5
user_list = [int(input('Введите число.\n')) for i in range(QUANTITY)] # Если чисел много, то консоль уплывает и список получается ненаглядным
print(user_list)
result_graphic = []
for i in range(len(user_list)):
    if i % 2 != 0:
        result_graphic.append('^'.center(len(str(user_list[i])) - 2))
    else:
        result_graphic.append(' ' * (len(str(user_list[i])) - 2))
        
print(result_graphic) #  нечетные позиции

result_list = sum([user_list[i] for i in range(len(user_list)) if i % 2 != 0]) # просуммируем их
print(result_list)

