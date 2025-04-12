import random

def guess_the_number():

    lower_bound = 1
    upper_bound = 100
    

    number_to_guess = random.randint(lower_bound, upper_bound)
    
    print("Welcome to the 'Guess the Number' Game!")
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}. Try to guess it!")
    

    guesses_taken = 0
    user_guess = None

  
    while user_guess != number_to_guess:

        user_guess = int(input("Enter your guess: "))
        guesses_taken += 1
        
     
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {guesses_taken} attempts.")
            break


guess_the_number()
