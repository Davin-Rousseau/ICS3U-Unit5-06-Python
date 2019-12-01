#!/usr/bin/env python3

# Created by: Davin Rousseau
# Created on: Nov 2019
# This program uses user defined functions
# To calculate volume of a cylinder


def round_off(numbers):
    # since lists are mutable, it can be changed
    numbers[0] = numbers[0] * (10 ** numbers[1]) + 0.5
    numbers[0] = int(numbers[0])
    numbers[0] = float(numbers[0])
    numbers[0] = numbers[0] / (10 ** numbers[1])


def main():
    # This checks if input is an integer and positive,
    # then calls function
    numbers = []
    # Input
    input_1 = input("Enter your number with decimals: ")
    input_2 = input("Enter how many decimal places you want to round: ")
    print("")

    try:
        chosen_number = float(input_1)
        round_number = int(input_2)
        if (chosen_number > 0 and round_number > 0):
            numbers.append(chosen_number)
            numbers.append(round_number)
            round_off(numbers)
            print(numbers[0])
        else:
            print("Invald input")
    except ValueError:
        print("Invalid input")


if __name__ == "__main__":
    main()
