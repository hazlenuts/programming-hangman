import random

def choose_word():
    words = ["python", "javascript", "ruby", "java", "swift", "php", "html", "css", "csharp", "go"]
    return random.choice(words)

def play_game():
    word = choose_word()
    word_letters = set(word)
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set()
  
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print(f"You have {lives}, lives left and you have used these letters: {' '.join(used_letters)}")

        word_list = [letter if letter in used_letters else '_' for letter in word]
        print(f"Current word: {' '.join(word_list)}")

        user_letter = input("Guess a letter: ").lower()[0]
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print("Letter is not in word.")
        
        elif user_letter in used_letters:
            print("You have already used that letter. Guess another one.")
        
        else:
            print("Invalid character. Please try again.")
    
    if lives == 0:
        print(f"Sorry, you died. The word was {word}")
    else:
        print(f"You guessed the word {word}!")

play_game()