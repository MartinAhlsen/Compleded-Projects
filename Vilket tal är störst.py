xnum1 = input("Välj ett nummer mellan 1 och 100: ")         # User input
xnum2 = input("Välj ett nummer mellan 1 och 100: ")
xnum3 = input("Välj ett nummer mellan 1 och 100: ")

def max_value2(num1, num2, num3):           # Return largest number
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num3:
        return  num2
    else:
        return num3

print(max_value2(float(xnum1),float(xnum2),float(xnum3)))   # Print largets number