class Dog:
    def __init__(self , name , breed ):
        self.name = name
        self.breed = breed #instance variable

    def bark(self):
        print(f"{self.name} is barking !")

if __name__ == "__main__":

    dog1 = Dog("Max", "Bulldog")
    dog1.bark()  # Output: Max is barking !
