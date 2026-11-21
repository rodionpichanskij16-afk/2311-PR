import random


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 100
        self.alive = True

    def to_study(self):
        print("Час вчитися")
        self.progress += 0.15
        self.gladness -= 5

    def to_sleep(self):
        print("Час спати")
        self.gladness += 3

    def to_chill(self):
        print("Час відпочити")
        self.gladness += 6
        self.progress -= 0.05
        self.money -= 20

    def to_work(self):
        print("Час на роботу, треба заробити грошей")
        self.money += 60
        self.gladness -= 4
        self.progress -= 0.02

    def is_alive(self):
        if self.progress < -0.5:
            print("Відраховано через погану успішність")
            self.alive = False
        elif self.gladness <= 0:
            print("Немає сил продовжувати.")
            self.alive = False
        elif self.money < -50:
            print("Банкрутство. Закінчилися всі кошти.")
            self.alive = False

    def end_of_day(self):
        print(f"Щастя = {self.gladness} | Прогрес = {round(self.progress, 2)} | Гроші = {self.money}")

    def live(self, day):
        day_info = f"День {day} з життя студента {self.name}"
        print(f"{day_info:=^50}")

        if self.money < 25:
            print("Закінчуються гроші. йду на роботу.")
            self.to_work()
        elif self.gladness < 20:
            print("Треба відпочити.")
            self.to_chill()
        elif self.progress < 3.0:
            print("Треба підтягнути навчання.")
            self.to_study()
        else:
            live_cube = random.randint(1, 4)
            if live_cube == 1:
                self.to_study()
            elif live_cube == 2:
                self.to_sleep()
            elif live_cube == 3:
                self.to_chill()
            elif live_cube == 4:
                self.to_work()

        self.end_of_day()
        self.is_alive()


student = Student(name="Родіон")

for current_day in range(1, 366):
    if not student.alive:
        break
    student.live(current_day)