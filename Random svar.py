import random
svar = ["There is no cake.", "The cake is a lie.",
        "Love the cube!", "We do what we must because we can.", "Apparature science!"]
text = ""

while text == "":
    input("Skriv en fråga: ")
    random_num = random.randint(1, 10)
    if random_num >= 5:
        print(svar[3])
    elif random_num == 4:
        print(svar[0])
    elif random_num == 4:
        print(svar[1])
    elif random_num == 4:
        print(svar[2])
    else:
        print(svar[4])