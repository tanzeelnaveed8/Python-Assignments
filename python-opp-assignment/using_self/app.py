class Student:
    def __init__(self , name , marks ):
        self.name = name 
        self.marks = marks

    def display(self):
            print(f"Name: {self.name} Marks: {self.marks}")

if __name__ == "__main__":
    s1 = Student("tanzeel bhai " , 19 )
    s1.display()