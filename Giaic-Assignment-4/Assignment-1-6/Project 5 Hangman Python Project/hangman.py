import random

def display_hangman(tries):
    stages = [
        '''
           --------
           |      |
           |
           |
           |
           |
           |
        -----''', '''
           --------
           |      |
           |      O
           |
           |
           |
           |
        -----''', '''
           --------
           |      |
           |      O
           |      |
           |
           |
           |
        -----''', '''
           --------
           |      |
           |      O
           |     /|
           |
           |
           |
        -----''', '''
           --------
           |      |
           |      O
           |     /|\\
           |
           |
           |
        -----''', '''
           --------
           |      |
           |      O
           |     /|\\
           |     /
           |
           |
        -----''', '''
           --------
           |      |
           |      O
           |     /|\\
           |     / \\
           |
           |
        -----'''
    ]
    return stages[tries]

def hangman():
    word_list = ['python', 'hangman', 'computer', 'programming', 'developer', 'challenge']
    word = random.choice(word_list)
    word_length = len(word)
    guessed_word = ['_'] * word_length
    guessed_letters = []
    tries = 0
    max_tries = 6
    
    print("Welcome to Hangman!")

    while tries < max_tries:
        print(display_hangman(tries))
        print('Current word: ' + ' '.join(guessed_word))
        print(f'Guessed letters: {", ".join(guessed_letters)}')

        guess = input("Guess a letter: ").lower()
        
      
        if guess in guessed_letters:
            print(f"You already guessed {guess}. Try again.")
            continue
        
       
        guessed_letters.append(guess)
        
     
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        
            for i in range(word_length):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            tries += 1
            print(f"Wrong guess! '{guess}' is not in the word.")
        

        if ''.join(guessed_word) == word:
            print("Congratulations, you've guessed the word!")
            break
    

    if tries == max_tries:
        print(display_hangman(tries))
        print(f"You've run out of tries! The word was: {word}")


hangman()
