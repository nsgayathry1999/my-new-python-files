class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def get_name(self):
        return self.name
    def get_salary(self):
        return self.salary
emp=Employee("Carls",50000)
print(f"Employee name:{emp.get_name()}")
print(f"Employee salary: ${emp.get_salary()}")
