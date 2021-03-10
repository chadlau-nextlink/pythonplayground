digi1 = float(input("Enter the first number: "))
op = input("Enter operator: ")
digi2 = float(input("Enter the second2 number: "))

if op == "+":
    print (digi1 + digi2)
elif op == "-":
    print (digi1 - digi2)
elif op == "*" or op == "x":
    print (digi1 * digi2)
elif op == "/":
    print (digi1 / digi2)
else:
    print("Please enter correct operator!")
