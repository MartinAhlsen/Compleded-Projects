def win():
    print("Du hade rätt!")
    exit()

def  print_clue(index):
    print("Ledtråd: " + str(clue[index]))

secret_word = "kaffe"
guess = ""
n_guesses = 4
clue = ["Drycken är varm", "Drycken är bäsk", "Drycken är svart"]
clue.reverse
n_clue = 0

while guess != secret_word and n_guesses > 0:
    guess = input("Vilken är den förbjudna drycken? (Du har {} gissningar kvar): ".format(n_guesses))
    
    if guess == secret_word:
        win()
    n_guesses -= 1
    print(" ")
    if n_guesses > 0:
        print_clue(n_clue)
    n_clue += 1

print("Du förlorade")

    #break och continue
