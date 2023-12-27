#task 1
temperature = float(input("Введите температуру в ℃:"))
if temperature < 15.5:
  print("ХОЛОДНО")
elif temperature > 28:
  print("ЖАРКО")
else:
  print("НОРМАЛЬНО")

#task 2
n = int(input("Введите количество строк: "))
s = ""
for i in range (0, n):
  s += str(input()) + "\n"
if ("кот" or "Кот") in s:
  print("МЯУ")
else:
  print("НЕТ")

#task 3
f = str(input()) #строка для считывания слов
max = ""
min = f #записываем первое слово в списке как минимальное по буквам
k = 0 #счетчик букв для проверки все ли буквы в содержатся в длинном слове
while f != "стоп":
  if len(f) > len(max):
    max = f
  if len(f) < len(min):
    min = f
  f = str(input())
  
for letter in min:
  if letter in max:
    k += 1
if k == len(min):
  print("ДА")
else:
  print("НЕТ")

#task 4
n = int(input("Введите количество покупок: "))
s = ""
for i in range (0, n):
  s += str(input()) + "\n"
print(s)

#task 5
s = str(input())
result = ""
for letter in s:
  result += letter*2
print(result)

#task 6
def great():
  name = str(input("Введите имя: "))
  lastname = str(input("Введите фамилию: "))
  print("Здравствуйте, {0} {1}.".format(name, lastname))
great()

#task 7
class LittleBell:
  def sound():
    print("ding")

#task 8
"""
Опыт программированя: изучала python на 1-2 курсе Бизнес-информатики, знаю некоторые основы. 
Данное задание трудностей не вызвало. Освежила знания по python, спасибо)
"""
