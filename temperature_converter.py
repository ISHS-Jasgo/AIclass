while True:
    menu = int(input("1) fahrenheit to celsius\n2) celsius to fahrenheit\n3) exit\n"))
    if menu == 1:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32.0) * 5 / 9
        # print result with f string in english
        print(f"Celsius {celsius} degrees is {fahrenheit} degrees Fahrenheit.")
    elif menu == 2:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9 / 5) + 32.0
        # print result with f string in english
        print(f"Fahrenheit {fahrenheit} degrees is {celsius} degrees Celsius.")
    else:
        break

# print exit message
print("Bye")
