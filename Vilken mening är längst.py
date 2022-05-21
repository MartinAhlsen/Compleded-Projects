phrase_1 = input("Write a sentence, finish with punctuation: ")
phrase_2 = input("Write another follow up sentence, finish with punctuation: ")

print(""
      "")

print(phrase_1 + " " + phrase_2)

print("\n----------------\n")

print("The lenght of phrase one is " + str(len(phrase_1)) + " characters long")
print("The lenght of phrase two is " + str(len(phrase_2)) + " characters long")

print("\n----------------\n")

x = len(phrase_1)
y = len(phrase_2)
if x > y:
    print("Phrase one is " + str(abs(len(phrase_1) - len(phrase_2))) + " characters longer than phrase two")
elif x == y:
    print("phrase_1 är lika lång som phrase_2")
else:
    print("Phrase one is " + str(abs(len(phrase_1) - len(phrase_2))) + " characters shorter than phrase two")