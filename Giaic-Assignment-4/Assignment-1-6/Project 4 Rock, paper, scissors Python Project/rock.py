import random

def play_game():
  
    choices = ['rock', 'paper', 'scissors']
    

    print("Welcome to Rock, Paper, Scissors!")


    while True:
     
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

     
        if user_choice not in choices:
            print("Invalid choice, please choose 'rock', 'paper', or 'scissors'.")
            continue


        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            print("You win!")
        else:
            print("Computer wins!")

     
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

play_game()