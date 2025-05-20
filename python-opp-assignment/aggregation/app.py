class Employee:
    def __init__(self, name):
        self.name = name
      

class Department:
    def __init__(self, employee ):
        self.employees = employee


    def show_employee(self):
       print(f"Employee Name: {self.employees.name}")

if __name__ == "__main__":
    emp1 = Employee("Jenny")
    dep = Department(emp1)
    dep.show_employee()
   