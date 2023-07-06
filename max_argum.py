#Программа свободные аргуменьы
#
# принимает случайные аргументы и строит слоаарь с ними

def high_arg(name, lastname, **info):
	unit = {}
	
	unit["Имя"] = name
	unit["Фамилия"] = lastname
	
	for key, value in info.items():
		unit[key] = value
	
	return unit

new = ("цвет", "белый")		
		
#Активация функции
show = high_arg(name="Федя", lastname="Ролин", пол="мужской", возраст=27)

print(show)

plus_age = int(input("Как старше: "))
new_age = show["возраст"] + plus_age

print(new_age)

input("\nНажмите Enter для выхода.")
		