# Step 1: Custom Exception Class
class InvalidAgeError(Exception):
    """Raised when the age is less than 18."""
    pass

# Step 2: Function to check age
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")
    else:
        print("Access granted. You are old enough!")

# Step 3: Test with try...except
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print("InvalidAgeError:", e)
except ValueError:
    print("Please enter a valid number.")
