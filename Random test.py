import random

array1 = []                                 # Kontroll av sannolikhet 
array2 = []      
array3 = []
array4 = []
array5 = []

tries = 100000

for tries in range(tries):                  # Placerar in resultat av N(tries) i arrays
    num_rand = (random.randint(1, 10))
    if num_rand >= 5:
        array5.append(num_rand)
    elif num_rand == 4:
        array4.append(num_rand)
    elif num_rand == 3:
        array3.append(num_rand)
    elif num_rand == 2:
        array2.append(num_rand)
    else:
        array1.append(num_rand)

print(len(array1))                          # Presenterar resultatet av varje array
print(len(array2))
print(len(array3))
print(len(array4))
print(len(array5))
print(len(array1)+len(array2)+len(array3)+len(array4)+len(array5))      # Summerar alla arrays
print(len(array5)/tries)       # Räknar ut hur många procent som hamnar i array5