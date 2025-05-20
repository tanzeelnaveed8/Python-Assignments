class Engine:
    def start(self):
        print("Engine has started")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()

if __name__ == "__main__":
    eng = Car()
    eng.start()