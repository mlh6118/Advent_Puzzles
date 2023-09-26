# Day 4: Camp Cleanup - Part 1
# This program will determine the number of elf pairs that have assignments
# that completely overlap one of their assignments.

import re

def Cleanup():

    with open('input.txt', 'r') as file:
        Lines = file.readlines()

        total = 0

        for line in Lines:
            line = line.strip()
            print(line)

            text = re.split('-|,', line)
            print(text)

            if int(text[0]) >= int(text[2]):
                if int(text[1]) <= int(text[3]):
                    print("True")
                    total = total + 1
                    continue

            if int(text[0]) <= int(text[2]):
                if int(text[3]) <= int(text[1]):
                    print("True")
                    total = total + 1
                    continue

        return total

print(Cleanup())
