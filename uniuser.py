#Эксклюзивный доступ 1.0
#
#Проверят наличие паролей iBlok0

#Импорт модуля секретной программы
#from secret import secret_prog
import random

#Импорт модуля и применение к нему псевдонима
from secret import secret_prog as spr

print("\tПрограмма уникальных пользователей")
user = ""
while not user:
	user = input("Логин: ")

password = ""
while not password:
	password = input("Пароль: ")
	
if user == "genius" and password == "um":
	print("Добро пожаловать 'гениальный' ")
	message = random.randint(0,99)
	print(message)
elif user == "hacker" and password == "run":
	print("Запуск секретнейшей программы!")
	spr()
else: 
	print("Прошу прощения но вы не уникальны!")
	


