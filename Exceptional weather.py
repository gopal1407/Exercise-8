#Task1

def get_temperature():
    try:
        # Ask the user to input temperature in Fahrenheit
        temp_fahrenheit = float(input("Please enter the temperature in Fahrenheit: "))
        return temp_fahrenheit
    except ValueError:
        # Handle case where the user input is not a valid number
        print("Error: Please enter a valid numeric value for temperature.")
        return None

# Example usage:
temperature = get_temperature()
if temperature is not None:
    print(f"You entered: {temperature}°F")

    #Task2

def fahrenheit_to_celsius(fahrenheit):
    try:
        # Convert Fahrenheit to Celsius
        celsius = (fahrenheit - 32) * 5 / 9
        return celsius
    except TypeError:
        # Handle case where input is not a number
        print("Error: The input temperature must be a number.")
        return None

def get_temperature():
    # Ask for user input
    try:
        temperature_input = input("Enter the temperature in Fahrenheit: ")
        
        # Convert the input to a float, handles non-numeric values
        fahrenheit = float(temperature_input)
        
        return fahrenheit
    except ValueError:
        # Handles the case when the input cannot be converted to a number
        print("Error: Please enter a valid number for temperature.")
        return None

# Main code to run the program
temperature = get_temperature()
if temperature is not None:
    celsius = fahrenheit_to_celsius(temperature)
    if celsius is not None:
        print(f"{temperature}°F is equal to {celsius:.2f}°C")

        #Task 3

def fahrenheit_to_celsius(fahrenheit):
    try:
        # Convert Fahrenheit to Celsius
        celsius = (fahrenheit - 32) * 5 / 9
        return celsius
    except TypeError:
        # Handle case where input is not a number
        print("Error: The input temperature must be a number.")
        return None

def get_temperature():
    # Ask for user input
    try:
        temperature_input = input("Enter the temperature in Fahrenheit: ")
        
        # Convert the input to a float, handles non-numeric values
        fahrenheit = float(temperature_input)
        
        return fahrenheit
    except ValueError:
        # Handles the case when the input cannot be converted to a number
        print("Error: Please enter a valid number for temperature.")
        return None

# Main code to run the program
temperature = get_temperature()
if temperature is not None:
    celsius = fahrenheit_to_celsius(temperature)
    if celsius is not None:
        # If conversion is successful, print the result in a user-friendly format
        print(f"{temperature} degrees Fahrenheit is {celsius:.2f} degrees Celsius.")
    else:
        print("Conversion failed due to invalid input.")
else:
    print("Please provide a valid temperature value.")

#Task4

def fahrenheit_to_celsius(fahrenheit):
    try:
        # Convert Fahrenheit to Celsius
        celsius = (fahrenheit - 32) * 5 / 9
        return celsius
    except TypeError:
        # Handle case where input is not a number
        print("Error: The input temperature must be a number.")
        return None

def get_temperature():
    # Ask for user input
    try:
        temperature_input = input("Enter the temperature in Fahrenheit: ")
        
        # Convert the input to a float, handles non-numeric values
        fahrenheit = float(temperature_input)
        
        return fahrenheit
    except ValueError:
        # Handles the case when the input cannot be converted to a number
        print("Error: Please enter a valid number for temperature.")
        return None

# Main code to run the program
try:
    temperature = get_temperature()
    if temperature is not None:
        celsius = fahrenheit_to_celsius(temperature)
        if celsius is not None:
            # If conversion is successful, print the result in a user-friendly format
            print(f"{temperature} degrees Fahrenheit is {celsius:.2f} degrees Celsius.")
        else:
            print("Conversion failed due to invalid input.")
    else:
        print("Please provide a valid temperature value.")
finally:
    # Thank the user for using the application
    print("Thank you for using the weather forecast application!")