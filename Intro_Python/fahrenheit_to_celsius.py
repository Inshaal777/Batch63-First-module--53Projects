def fahrenheit_to_celsius(degrees_fahrenheit):
    return (degrees_fahrenheit - 32) * 5.0/9.0
def main():
    try:
        fahrenheit_input = input("Enter temperature in Fahrenheit: ")
        degrees_fahrenheit = float(fahrenheit_input)
        degrees_celsius = fahrenheit_to_celsius(degrees_fahrenheit)
        print(f"Temperature: {degrees_fahrenheit}F = {degrees_celsius}C")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == '__main__':
    main()