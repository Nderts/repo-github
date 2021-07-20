
# a = 45
# b = 10
# input_c = input('введите любое нечетное число: ')
# print(a)
# print(b)
# print(input_c)

# input_a = input("введите время в секундах: ")
# a = (int(input_a) // 6000)
# b = ((int(input_a) % 6000) // 60)
# c = (int(input_a) - ((a*6000)+(b*60)))
# print(a,":",b,":",c)


# input_a = input("введите произвольное целое число от 1 до 9: ")
# n = int(input_a)
# a = (n + n*10+n + n*100+n*10+n)
# print(a)



# a = input("введите произвольное целое положительное число: ")
# n = int(a) % 10
# a = int(a) // 10
# while a > 0:
#     if a % 10 > n:
#         n = a % 10
#     a = a // 10
# print (n)



# a = int(input("введите значение выручки фирмы: "))
# b = int(input("введите значение издержек фирмы: "))
# if a > b:
#     print ('прибыль')
# else:
#     print ('убыток')



a = int(input("в первый день спортсмен пробежал: "))
b = int(input("требуемый результат не менее: "))
n = 1
while a < b:
    a = a * 1.1
    n = n + 1
print (n)




