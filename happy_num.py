#Счасиливые числа 1.2
#
#Игрок пишет число, программа проверяет счастливое ли оно

number = input("Напишите ваше число: ")

side = len(number) // 2

l_side = sum([int(num) for num in number[:side]])

r_side = sum([int(num) for num in number[-side:]])

if l_side == r_side:
	print("Ваши чиселки счастливые!")
else:
	print("Это число обыкновено")

print(l_side)

print(r_side)