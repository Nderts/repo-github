a = input("введите произвольное целое положительное число: ")
n = int(a) % 10
a = int(a) // 10
while a > 0:
    if a % 10 > n:
        n = a % 10
    a = a // 10
print (n)