class counter:
    count = 0

    def __init__(self):
        counter.count += 1
        
    @classmethod
    def display_count(cls):
        print(f"object created : {cls.count}")

if __name__ == "__main__":
    c1 = counter()
    c2 = counter()
    c3 = counter()
    c4 = counter()
    c5 = counter()
    c6 = counter()
    c7 = counter()
    c8 = counter()
    c9 = counter()
    c10 = counter()

    counter.display_count()  

