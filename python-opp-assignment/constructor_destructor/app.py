class Logger:
    def __init__(self):
        print("object created sucessfully ")

    def __del__ (self):
        print("object is destoryed now")

if __name__ == "__main__":
    log = Logger() 
    del log