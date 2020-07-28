# -*-coding:utf-8-*-

def total(num):
    i = num // 5
    if num % 5 != 0:
        i += 1
    return i * 5


print(total(5))
print(total(11))
