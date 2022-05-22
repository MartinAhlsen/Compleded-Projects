is_male = True              # From input boolean
is_female = False
tall = True

male = input("Are you male? Y/N: ")         # Personal data input
female = input("Are you female? Y/N: ")
length = input("How tall are you in cm? : ")

if male == "Y" or male == "y":      # Gender Male
    is_male = True
else:
    is_male = False

if female == "Y" or female == "y":      # Gender female
    is_female = True
else:
    is_female = False

if float(length) >= 180:        # Short or tall
    tall = True
else :
    tall = False



if is_male and not is_female:           # phrase_1 determines gender
    phrase_1 = ("You are male")
elif is_female and not is_male:
    phrase_1 = ("You are female")
else:
    phrase_1 = ("You are non binary")
if tall:
    phrase_2 = (", tall and handsome!")     # phrase_2 determines tall or short
else:
    phrase_2 = (", short and beautiful!")

print("\n" + phrase_1 + phrase_2)

