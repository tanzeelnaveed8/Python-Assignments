# Step 1: Decorator definition
def add_greeting(cls):
    # Step 2: Add greet method dynamically to the class
    def greet(self):
        return "Hello from Decorator!"
    
    cls.greet = greet  # Add method to class
    return cls         # Return modified class

# Step 3: Apply decorator to Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Step 4: Test the decorated class
p = Person("Ali")
print(p.greet())  # Output: Hello from Decorator!
