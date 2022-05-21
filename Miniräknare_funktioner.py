print("Fyra räknesätten och procent")


operator = input("\n"                                                   #Välj räknesätt
              "Skriv + för addition\n"
              "Skriv - för subtraktion\n"
              "Skriv * för multiplikation\n"
              "Skriv / för division\n"
             "Skriv % för procent\n"
              "Vilket räknesätt vill du använda?: ")
tal1 = float(input("Vilket är det första talet du vill använda: "))     #Skriv första talet
tal2 = float(input("Vilket är det andra talet du vill använda: "))      #Skriv andra talet

print("\nResultat")                                                     #Uträkningen
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


print("\n----------------\n")                                           #Skriver ut resultatet