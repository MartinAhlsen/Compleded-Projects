import random
svar = ["There is no cake", "The cake is a lie",
        "Love the cube!", "Jag älskar Denise!", "Apparature science!"]
abc = ""

# while abc == "":
#     input("Skriv något: ")
#     random_num = random.randint(1, 10)
#     if random_num >= 5:
#         print(svar[3])
#     elif random_num == 4:
#         print(svar[0])
#     elif random_num == 4:
#         print(svar[1])
#     elif random_num == 4:
#         print(svar[2])
#     else:
#         print(svar[4])

# Kontroll av sannolikhet
var1 = []
var2 = []
var3 = []
var4 = []
var5 = []

tries = 100000

for tries in range(tries):
    heja = (random.randint(1, 10))
    if heja >= 5:
        var5.append(heja)
    elif heja == 4:
        var4.append(heja)
    elif heja == 3:
        var3.append(heja)
    elif heja == 2:
        var2.append(heja)
    else:
        var1.append(heja)

print(len(var1))
print(len(var2))
print(len(var3))
print(len(var4))
print(len(var5))
print(len(var1)+len(var2)+len(var3)+len(var4)+len(var5))
print(len(var5)/tries)
