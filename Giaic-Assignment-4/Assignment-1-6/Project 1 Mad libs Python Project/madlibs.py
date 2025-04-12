def mad_libs_game():
    print("Welcome to the Mad Libs Game!")
    
  
    noun1 = input("Enter a noun: ")
    adjective1 = input("Enter an adjective: ")
    verb1 = input("Enter a verb (past tense): ")
    noun2 = input("Enter another noun: ")
    place = input("Enter a place: ")
    animal = input("Enter an animal: ")
    adjective2 = input("Enter another adjective: ")
    
   
    story = f"Today, I went to the {place} to see a {animal}. It was a very {adjective1} day! " \
            f"I saw a {adjective2} {noun1} and decided to {verb1} with it. " \
            f"It was so much fun! Later, I met a {noun2} and we laughed together for hours."
    
  
    print("\nHere is your Mad Libs story:")
    print(story)


mad_libs_game()
