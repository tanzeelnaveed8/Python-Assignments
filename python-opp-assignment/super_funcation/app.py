class Person:
    def __init__(self , name):
        self.name = name
        

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
       

    def display(self):
            print(f"Teacher {self.name} teaches {self.subject}")

if __name__ == "__main__":
    teacher = Teacher("Miss Areeba", "Science")
    teacher.display()
   