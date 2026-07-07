#学习git commad
print("hello world")
cubes = [i ** 3 for i in range(10)]
for number in range(100, 1000):
    hundreds = number // 100
    tens = number // 10 % 10
    ones = number % 10
    if cubes[hundreds] + cubes[tens] + cubes[ones] == number:
        print(number)
#二次修改