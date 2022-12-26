c_degrees = int(input("enter celsius degrees. "))

def convert_celsius_to_fahrenheit(cel):
    return (1.8*cel+32)
    
    
print("The Fahrenheit equivalent of " + str(c_degrees) + " degrees Celsius is " + str(convert_celsius_to_fahrenheit(c_degrees)) + "!.")