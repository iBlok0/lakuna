#Модуль недели
#
#Время или time

import time

#Возвращение текущего времени Unix
ut = time.time()

#Преобразование в обычный вид
qt = time.ctime()

print(ut)

print(qt)

ft = time.strftime("%d_%B_%Y")
print(ft)

caffe_days = {}
caffe_days[ft] = "Список заказов за этот день."

new_day = time.strftime("%d")
new_day = int(new_day) + 1
print(new_day)
nt = time.strftime("_%B_%Y")

if new_day < 10:
	st = "0" + str(new_day) + nt
else:
	st = str(new_day) + nt

caffe_days[st] = "Это список заказов на завтрашний день"

for key, value in caffe_days.items():
	print(key, " - ", value)

print(caffe_days)

td = time.gmtime(5750000050)
print(td)

tm = time.mktime(td)
print(tm)