def make_hangman(secret_word):
    guesses = []
    display = ["_"] * len(secret_word)

    def hangman_closure():
        while "_" in display:
            print("Current word: " + " ".join(display))
            letter = input("Guess a letter: ").lower()

            if not letter or len(letter) != 1:
                print("Please guess a single letter.")
                continue

            guesses.append(letter)

            for i, char in enumerate(secret_word):
                if char == letter:
                    display[i] = char

            if "_" not in display:
                print("You won! The word was:", secret_word)
                break

    hangman_closure()

make_hangman("google")
