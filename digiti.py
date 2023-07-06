#Загадай число ИИ 1.0
#
#Человек загадывает число а ИИ будет его отгадывать

#Импорт модулей
from random import*
import time

#Вводные данные
start = 1
finish = 100
tries = 1
#Число от человека
print('\tЗагадай число ИИкту\n')
number = int(input('Человечашка придумывай чиселко: '))
time.sleep(1)
print('Это невероятно просто!')
cpu_answer = randint(start,finish)
while number != cpu_answer:
	print('Это число - ', cpu_answer)
	if cpu_answer > number:
		print('Твои цифровые мозги из поленьев, нужное число меньше, оно даже написно выше. Попробуй еще раз.')
		finish = cpu_answer - 1
		tries +=1
		
	if cpu_answer < number:
		print('Хоть ты и интелект, но деревянный, число крупнее твоего. Пробуй еще раз.')
		start = cpu_answer + 1
		tries += 1
		

			
	cpu_answer = randint(start, finish)
	print('ой, это все равно возможно!\n')
	#задержка в секунду
	time.sleep(1)

	if cpu_answer == number:
		print('Это число - ', cpu_answer)
		print('Фига се, железный ум, ты справился! Молодечик!')
		print('Тебе понадобилось' , tries ,'попыток')
		if tries > 5: 
			print('Нужно развиваться лучше, думать лучше')
		if tries <= 5:
			print('Крут! реально быстро')
		

input('Нажмите интер, чтобы выйти.')