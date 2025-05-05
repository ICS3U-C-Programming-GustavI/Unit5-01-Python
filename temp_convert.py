#!/usr/bin/env python3
# Created by: Gustav I
# Created on: April 19, 2025
# This program defines a function and converts user celsius to fahrenheit.


def fahrenheit():
    try:
        # Ask the user to enter the temperature in Celsius
        celsius = float(input("Enter temperature in Celsius: "))

        # Convert the temperature to Fahrenheit
        fahrenheit = (9 / 5) * celsius + 32

        # Display the result
        print("Temperature in Fahrenheit is:", fahrenheit)

    except ValueError:
        print("Invalid input! Please enter a numeric value.")


def main():
    fahrenheit()  # Call the fahrenheit conversion function


# Call the main function
if __name__ == "__main__":
    main()
