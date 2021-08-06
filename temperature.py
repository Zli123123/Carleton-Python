
def Celsius_to_Kelvin(s:float)->float :
    return s + 273.15
def Celsius_to_Fahrenheit(s:float)->float :
    return (s * 9/5) + 32
def Kelvin_to_Celsius(s:float)->float :
    return s - 273.15
def Kelvin_to_Fahrenheit(s:float)->float :
    return (s - 273.15) * 9/5 +32
def Fahrenheit_to_Celsius(s:float)->float :
    return (s - 32) * 5/9
def Fahrenheit_to_Kelvin(s:float)->float :
    return (s - 32) * 5/9 +273.15


String = input("Temperature: ")

unit = String[-1]
unit1 = unit.upper()
value = float(String[:-1])
count = 0
print(unit1, value)
if unit1 != "K":
    count += 1
    print("y")
if unit1 != "F":
    count += 1
    print("d")
if unit1 != "C":
    count += 1
    print("d")
if count == 3:
    print("incorrect unit")
if count == 2:
    print("o")
    if unit1 == 'C':
        print("Kelvin: ", Celsius_to_Kelvin(value))
        print("Fahrenheit: ", Celsius_to_Fahrenheit(value))
    if unit1 == 'K':
        print("celsius: ", Kelvin_to_Celsius(value))
        print("Fahrenheit: ", Kelvin_to_Fahrenheit(value))    
    if unit1 == 'F':
        print("Celsius: ", Fahrenheit_to_Celsius(value))
        print("Kelvin: ", Fahrenheit_to_Kelvin(value))    