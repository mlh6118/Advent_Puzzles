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

            text = re.split('-|,', line)

            if int(text[0]) >= int(text[2]):
                if int(text[1]) <= int(text[3]):
                    total = total + 1
                    continue

            if int(text[0]) <= int(text[2]):
                if int(text[3]) <= int(text[1]):
                    total = total + 1
                    continue

        return total

print(Cleanup())


def Cleanup_Overlap():
    with open('input.txt', 'r') as file:
        Lines = file.readlines()

        overlap = False
        total_overlaps = 0

        for line in Lines:
            line = line.strip()

            text = re.split('-|,', line)

            if int(text[0]) >= int(text[2]):
                if int(text[0]) <= int(text[3]):
                    overlap = True
                    total_overlaps = total_overlaps + 1
                    continue
            elif int(text[1]) <= int(text[3]):
                if int(text[1]) >= int(text[2]):
                    overlap = True
                    total_overlaps = total_overlaps + 1
                    continue
            elif int(text[2]) <= int(text[0]):
                if int(text[2]) <= int(text[1]):
                    overlap = True
                    total_overlaps = total_overlaps + 1
                    continue
            elif int(text[3]) <= int(text[1]):
                if int(text[3]) >= int(text[0]):
                    overlap = True
                    total_overlaps = total_overlaps + 1
                    continue

    return total_overlaps

print(Cleanup_Overlap())