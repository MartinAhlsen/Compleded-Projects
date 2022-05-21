def max_value(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num3:
        return  num2
    else:
        return num3

print(max_value(1,2,3))


xnum1 = input("Välj ett nummer mellan 1 och 100: ")
xnum2 = input("Välj ett nummer mellan 1 och 100: ")
xnum3 = input("Välj ett nummer mellan 1 och 100: ")

def max_value2(num4, num5, num6):
    if num4 >= num5 and num4 >= num6:
        return num4
    elif num5 >= num6:
        return  num5
    else:
        return num6

print(max_value2(float(xnum1),float(xnum2),float(xnum3)))