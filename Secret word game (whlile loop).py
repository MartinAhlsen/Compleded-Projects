def win():              # After correct guess - exit game
    print("Du hade rätt!")
    exit()

def  print_clue(index):
    print("Ledtråd: " + str(clue[index]))

secret_word = "kaffe"   # The correct answer
guess = ""          # Input from user
n_guesses = 4       #Number of guesses left
clue = ["Drycken är varm", "Drycken är bäsk", "Drycken är svart"]   # Clues
clue.reverse
n_clue = 0      # Clue to be printed

while guess != secret_word and n_guesses > 0:       # Game start
    guess = input("Vilken är den förbjudna drycken? (Du har {} gissningar kvar): ".format(n_guesses))
    
    if guess == secret_word:    # Victory condition
        win()
    n_guesses -= 1      # Remove a guess
    print(" ")
    if n_guesses > 0:
        print_clue(n_clue)
    n_clue += 1         # Add to n_clue to present the next clue in the clue array

print("Du förlorade")   # If no guesses left
