#Тестирование кода из программы практикума  яндекса.               
message = 'Роботы скоро захватят мир!'
print(message.replace('захватят' , 'спасут')) 

print('Я твоя программа, мне тут нравится!')

print(100 + int("500"))

#https://practicum.yandex.ru/trainer/backend-developer/lesson/4ebc867c-10b0-49a4-b128-f3962ef1266d/

#функция range с отрицательным шагом
chisla = range(10, -10, -1)
for i in chisla:
    print(i, end=" ")
print()   

#reversed = Перевёрнутый
for i in reversed(chisla):
    print(i, end=" ")
print()
#логический ответ в переменой

check = (2*2 == 4)
print(check)

#функция type для вывода типа елемента 
print(type(check))