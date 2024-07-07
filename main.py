#!/usr/bin/env python

""""A simple program that asks a user for two numbers, and what operator theyd like to use on them and then gives a result"""

def evaluate_operation(operator_chosen, first_number, second_number):
    """Evaluates operation between numbers input by user and returns result"""

     # Check which operator was chosen for operation
    if int(operator_chosen) == 1:
        # Evaluate input and save it as result
        result = int(first_number) + int(second_number)
        print(f"\n{first_number} + {second_number} = {result}")
        return result
    elif int(operator_chosen) == 2:
        # Evaluate input and save it as result
        result = int(first_number) - int(second_number)
        print(f"\n{first_number} - {second_number} = {result}")
        return result
    elif int(operator_chosen) == 3:
        # Evaluate input and save it as result
        result = int(first_number) * int(second_number)
        print(f"\n{first_number} * {second_number} = {result}")
        return result
    elif int(operator_chosen) == 4:
        # Evaluate input and save it as result
        result = int(first_number) / int(second_number)
        print(f"\n{first_number} / {second_number} = {result}")
        return result
    else:
        print("You didnt choose properly")


def next_steps(first_number, second_number):
    """After the result of operation is given to the user determines what theyd like to do next"""
    # Ask if theyd like to clear the calculator and start again, use the result for additional operations, or quit the program
    what_to_do_next = "\nWould you like to?..."
    what_to_do_next += "\n1.Clear the calculator and make another operation"
    what_to_do_next += "\n2.Make another operation based on the most recent result"
    what_to_do_next += "\n3.Quit the program?"
    what_to_do_next += "\nYour choice: "

    what_to_do_next = input(what_to_do_next)
    # If theyd like to clear
    if int(what_to_do_next) == 1:
        # Clear the user input and result and start from the beginning of the program
        first_number, second_number, result = None, None, None
    # Else if theyd like to use the result for additional operations
    elif int(what_to_do_next) == 2:
        # Set the result as the first input and start the program again.
        first_number = result
        second_number, result = None, None
    #Else if theyd like to quit
    elif int(what_to_do_next) == 3:
        # Quit the program
        return "Break"


def main():
    """Main entrypoint to execute the calculator"""

    first_number = None
    second_number = None
    result = None

    print("This program is a simple calculator")
    
    # Calculator loop
    while True:
        # Check first input does not have a value from last calculation
        if not first_number:
            # Ask user for first number
            first_number = input("\nFirst operand: ")
        # Ask user for operation theyd like to utilize (add, subtract, multiply, divide)
        operator_prompt = "What operation are you using?"
        operator_prompt += "\n1.add, 2.subtract, 3.multiply, or 4.divide?(Enter a number from 1 - 4)"
        operator_prompt += "\nYour choice: "
        operator_chosen = input(operator_prompt )
        # Ask user for second number
        second_number = input("Second operand: ")
            
        evaluate_operation(operator_chosen, first_number, second_number)

        continue_or_break = next_steps()

        if continue_or_break == 'Break':
            break
        
        
if __name__ == "__main__":
    main()

    