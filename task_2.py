#task_1
#Пользователь сначала вводит количество чисел, а затем вводит сами числа, ваша задача отсортировать введенные пользователем числа и вывести их в обратном порядке.
n = int(input())
s_list = []
for i in range(0, n):
  s_list.append(int(input()))
s_list = sorted(s_list)
s_list.reverse()
print(s_list)

#task_2
#Напишите программу, которая проводит первичную обработку неких сложных и глючных логов. Нужно удалить сочетание «%%» в начале некоторых строк и удалить строки, начинающиеся с «###».

n = int(input())
s = ""

for i in range (0, n):
  k = str(input())
  if k[:2]=="%%":
    k = k[2:]
  if k[:3] != "###":
    s += k + "\n"
print(s)

#task_3
#Напишите программу, которая считывает список чисел, а затем выводит сумму в диапазоне от заданного до заданного. При этом в программе не должно использоваться обращение к элементам по индексу

n = int(input())
s_list = []

for i in range (0, n):
  s_list.append(int(input()))

p = int(input())
q = int(input())

count = 0
s = 0 # sum numbers
for e in s_list:
  count += 1
  if (count >= p) and (count <= q):
    s += e
print(s)

#task_4
#В школе №13 отличников по программированию награждают поездкой в Артек, но счастливых учеников может быть больше, чем свободных мест - ваша задача 
#определить отличников и если их больше чем свободных мест, то отсортировать их по фамилии и вывести тех, кто едет.
def Artek (s, n):
  s = s.split(', ')
  artek = []
  for e in s:
    if e[-1] == '5':
      artek.append(e[:-2])
  artek = sorted(artek)
  if len(artek) > n:
    return(", ".join(artek[0:n]))
  else:
    return(", ".join(artek))

s = str(input())#список студентов
n = int(input())#количество заявок
b = Artek(s,n)
print(b)

#task_5*
#Написать программу, которая просит пользователя ввести пароль и подтвердить его (как при обычной регистрации). Пароль должен соответствовать следующим требованиям:
#1)В пароле должны быть буквы (Заглавные и прописные)
#2)В пароле должны быть цифры
#3)В пароле должен быть хотя бы один спец. символ @#$%&*().,-_+
#4)Длина пароля не менее 8 символов

def password_level(s):
  if len(s)<8:
    return("Недопустимый пароль")
  if s.isdigit() == True or s.islower() == True or s.isupper() == True:
    return("Ненадежный пароль")
  if s.isalpha() == True:
    return("Слабый пароль")
  else:
    return("Надежный пароль")

b = ""
while b != "Надежный пароль":
  password = str(input("Придумайте пароль: "))
  b = password_level(password)
  print(b)

password_1 = ""
while password != password_1:
  password_1 = str(input("Введите пароль повторно: "))
  if password != password_1:
    print("Пароли НЕ совпадают")
    
print("Пароли совпадают")
