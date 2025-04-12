import random

NUM_ROUNDS = 5 

def get_valid_guess():
    guess = input("Do you think your number is higher or lower than the computer's?: ").lower()
    while guess not in ['higher', 'lower']:
        guess = input("Please enter either 'higher' or 'lower': ").lower()
    return guess

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    score = 0

    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")

        your_num = random.randint(1, 100)
        computer_num = random.randint(1, 100)

        print(f"Your number is {your_num}")
        guess = get_valid_guess()

        if your_num == computer_num:
            print(f"Aww, that's incorrect. The computer's number was {computer_num}")
        elif guess == 'higher' and your_num > computer_num:
            print(f"You were right! The computer's number was {computer_num}")
            score += 1
        elif guess == 'lower' and your_num < computer_num:
            print(f"You were right! The computer's number was {computer_num}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_num}")

        print(f"Your score is now {score}")
        print() 

    print("Thanks for playing!")

    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

main()
