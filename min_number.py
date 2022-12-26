#!/usr/bin/env python3

# Created by: Kaitlyn Ip
# Created on: Dec 2022
# This program finds the smallest number in a list of random numbers

import random


def calculate_smallest_num(list_of_numbers):
    # This function identifies the largest integer
    minimum = list_of_numbers[0]

    for loop_counter in range(1, len(list_of_numbers)):
        if list_of_numbers[loop_counter] < minimum:
            minimum = list_of_numbers[loop_counter]

    return minimum


def main():
    # this function uses an array
    random_nums = []

    # process
    for loop_counter in range(0, 10):
        a_random_num = random.randint(1, 100)  # a number between 1 and 100
        print("The random number is: {0}".format(a_random_num))
        random_nums.append(a_random_num)
    print("")

    smallest_int = calculate_smallest_num(random_nums)
    print("The smallest random number is: {0}.".format(smallest_int))

    print("\nDone.")


if __name__ == "__main__":
    main()
