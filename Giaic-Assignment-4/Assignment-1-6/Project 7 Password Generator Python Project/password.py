import random
import string

def generate_password(length=12):
   
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    all_characters = lower + upper + digits + special_characters

  
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")

   
    length = int(input("Enter the desired password length: "))


    password = generate_password(length)

    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
