class Employee :
    def __init__(self , name , salary , ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

if __name__ == "__main__":
    emp = Employee("Tanzeel" , 5000 , 1234)
    print("public name :", emp.name)
    print("protected salary :" , emp._salary)
    try:
        print("prvate ssn :", emp.__ssn)
    except AttributeError :
        print(" this data is private")






