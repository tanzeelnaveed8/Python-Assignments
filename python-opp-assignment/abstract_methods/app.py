from abc import abstractmethod


class Area :
    @abstractmethod
    def __init__(self):
        pass


class rectangle(Area):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    

if __name__ == "__main__":
    rect = rectangle(10, 5)
    print(f"Area of rectangle: {rect.area()}")  # Output: Area of rectangle: 50