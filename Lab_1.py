class Pupa:
  def __init__(self):
    self.count = 0

  def do_work(self, spisok1, spisok2):
    spisok = []
    self.count += len(spisok1)
    for i in range (0, len(spisok1)):
      spisok.append(spisok1[i]+spisok2[i])
    print("Работа Пупы:", spisok)
    return spisok

  def take_salary(self):
    salary = 1*self.count
    print("Пупа получил зарплату: ", salary)
    return salary


class Lupa:
  def __init__(self):
    self.count = 0

  def do_work(self, spisok1, spisok2):
    spisok = []
    self.count += len(spisok1)
    for i in range (0, len(spisok1)):
      spisok.append(spisok1[i]-spisok2[i])
    print("Работа Лупы: ", spisok)
    return spisok

  def take_salary(self):
    salary = 5*self.count
    print("Лупа получил зарплату: ", salary)
    return salary


class Accountant():
  def give_salary(self, worker):
    return worker.take_salary()



if __name__=="__main__":
    acc = Accountant()
    lupa = Lupa()
    lupa.do_work([1, 2, 2], [2, 4, 1])
    lupa.do_work([1, 3, 5], [1, 1, 1])
    lupa.do_work([1, 2, 4], [2, 4, 6])
    pupa = Pupa()
    pupa.do_work([1, 2, 2], [2, 4, 1])
    acc.give_salary(lupa)
    acc.give_salary(pupa)
