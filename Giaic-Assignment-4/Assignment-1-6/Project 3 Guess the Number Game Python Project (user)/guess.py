def guess_the_number():

    lower_bound = 1
    upper_bound = 100


    print("Welcome to the 'Guess the Number' Game!")
    print(f"Think of a number between {lower_bound} and {upper_bound} and I will try to guess it.")
    print("Respond with 'too high', 'too low', or 'correct' after each guess.")

   
    guesses_taken = 0
    user_feedback = ""

    while user_feedback != "correct":

        computer_guess = (lower_bound + upper_bound) // 2
        guesses_taken += 1

      
        user_feedback = input(f"Is your number {computer_guess}? ").lower()

        if user_feedback == "too low":
            lower_bound = computer_guess + 1
        elif user_feedback == "too high":
            upper_bound = computer_guess - 1
        elif user_feedback == "correct":
            print(f"Yay! I guessed your number {computer_guess} in {guesses_taken} attempts.")
        else:
            print("Please enter 'too high', 'too low', or 'correct'.")


guess_the_number()