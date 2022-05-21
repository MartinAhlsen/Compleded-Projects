is_male = True
is_female = False
tall = True

male = input("Are you male? Y/N: ")
female = input("Are you female? Y/N: ")
length = input("How tall are you in cm? : ")

if male == "Y" or male == "y":
    is_male = True
else:
    is_male = False
if female == "Y" or female == "y":
    is_female = True
else:
    is_female = False
if float(length) >= 180:
    tall = True
else :
    tall = False



if is_male and not is_female:
    phrase_1 = ("You are male")
elif is_female and not is_male:
    phrase_1 = ("You are female")
else:
    phrase_1 = ("You are non binary")
if tall:
    phrase_2 = (", tall and handsome!")
else:
    phrase_2 = (", short and beautiful!")

print("\n" + phrase_1 + phrase_2)

