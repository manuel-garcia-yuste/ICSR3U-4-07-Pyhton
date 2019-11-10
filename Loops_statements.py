#!/usr/bin/env python3

# Created by: Manuel Garcia Yuste
# Created on : November 2019
# This program do a for loop


def main():

    # input
    input("Press enter to start. ")

    # variable
    keep_upper = 0

    # process & output
    for number in range(1000, 2001):
        print(number, sep="", end=" ")
        if keep_upper % 5 == 4:
            print("")
        keep_upper = keep_upper + 1


if __name__ == "__main__":
    main()
