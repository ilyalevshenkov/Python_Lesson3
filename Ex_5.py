#Задание 5 . Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#Пример:
#- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def get_fiboncci(n):
    fib_list = []
    a, b = 1, 1
    for i in range(n-1):
        fib_list.append(a)
        a, b = b, a + b
    a, b = 0, 1
    
    for i in range (n):
        fib_list.insert(0, a)
        a, b = b, a - b
        
    return fib_list

n = int(input('Веедите число:  ')) + 1
fib_list = get_fiboncci(n)
print(fib_list)
