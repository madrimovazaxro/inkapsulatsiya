import os
os.system("cls")

class Employee:
    def __init__(self, name, employee_id, hourly_rate = 15.0):
        self.name = name
        self.employee_id = employee_id
        self.__working_hours = []
        self.hourly_rate = hourly_rate #obyekt berganda yangi qiymat yozsak o'zgaradi, agar bermasak 15.0 olib ketadi
    def long_hours(self, hour, parol):
        if parol == "qwerty" and 0 <= hour <= 24:
            self.__working_hours.append(hour)
            return True
        else:
            return False
    def total_hours(self, parol):
        if parol == "qwerty":
            return int(sum(self.__working_hours))
        else:
            return "Xato parol kiritildi!"
    def calculate_salary(self, parol):
        x = self.total_hours(parol)
        if isinstance(x, str):
            print(x)
            return
        else:
            return x * self.hourly_rate
    def reset_hours(self, parol):
        if parol == "qwerty":
            self.__working_hours.clear()
    
employee = Employee("Javlon", "E101", hourly_rate = 20.0)

print(employee.long_hours(8, "qwerty"))   	# True
print(employee.long_hours(9, "qwerty"))   	# True
print(employee.long_hours(10, "qwerty"))  	# True
print(employee.long_hours(25, "qwerty"))  	# False 

print(employee.total_hours("qwerty"))       	# 27
print(employee.calculate_salary("qwerty"))  	# 540.0 (27 * 20)

employee.reset_hours("qwerty")
print(employee.total_hours("qwerty"))       	# 0
print(employee.calculate_salary("qwerty"))  	# 0.0





        
