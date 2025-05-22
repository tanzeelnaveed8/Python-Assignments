class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        self.current = self.start
        return self  # Iterator object itself

    def __next__(self):
        if self.current < 0:
            raise StopIteration  # End of iteration
        value = self.current
        self.current -= 1
        return value

# Test in a for loop
for num in Countdown(5):
    print(num)
