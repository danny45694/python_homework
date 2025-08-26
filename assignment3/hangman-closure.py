def make_hangman(secret_word):
    guesses = []   
    
    def hangman_closure(letter):
        nonlocal guesses
        guesses.append(letter)
        
        
        revealed = ''.join(ch if ch in guesses else '_' for ch in secret_word)
        print(revealed)
        
      
        if '_' not in revealed:
            print("You guessed the word!")
            return True
        else:
            return False
    
    return hangman_closure

secret_word = input("Enter a secret word: ")
game = make_hangman(secret_word)

while True:
    letter = input("Guess a letter: ")
    done = game(letter)
    if done:
        break