import os
os.system("cls")

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.__grades = []
    def add_grade(self, grade, parol):
        if parol == "qwerty" and grade in range (0,101) :
            self.__grades.append(grade)
        elif parol != "qwerty":
            print("Noto'g'ri parol kiritildi!")
        else:
            print("Xato: noto'g'ri baho!")
    def calculate_average(self, parol):
        if parol == "qwerty":
            average = sum(self.__grades)/len(self.__grades)
            return  average
        else:
            return "Noto'g'ri parol kiritildi!"

    def get_status(self, parol):
        x = self.calculate_average(parol)
        if isinstance(x, str):
            print(x)
            return

        if 90 <= x <= 100 and x in int():
            print("A'lo")
        elif 80 <= x <= 89:
            print("Yaxshi")
        elif 70 <= x <= 79:
            print("Qoniqarli")
        else:
            print("Qoniqarsiz")

student = Student("Nodira", "S123")
student.add_grade(85, "qwerty")
student.add_grade(90, "qwerty")
print(student.calculate_average("qwerty"))
student.get_status("qwerty")
student.add_grade(150, "qwerty")
