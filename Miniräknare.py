print("Fyra räknesätten och procent")                   # Information om funktioner till användaren


operator = input("\n"                                           # Input från andvändren
              "Skriv + för addition\n"                          # Räknesätt
              "Skriv - för subtraktion\n"
              "Skriv * för multiplikation\n"
              "Skriv / för division\n"
             "Skriv % för procent\n"
              "Vilket räknesätt vill du använda?: ")
tal1 = float(input("Vilket är det första talet du vill använda: "))     # Användaren väljer två nummer
tal2 = float(input("Vilket är det andra talet du vill använda: "))

print("\nSvar")             # Miniräknaren - ränkar och presenterar svaret
if operator == "+":
    print(tal1 + tal2)
elif operator == "-":
    print(tal1 - tal2)
elif operator == "*":
    print(tal1 * tal2)
elif operator == "/":
    print(tal1 / tal2)
elif operator == "%":
    print(tal1 / 100 * tal2)
else:
    print("faulty input")

print("\n----------------\n")       # Skapar en skiljelinje