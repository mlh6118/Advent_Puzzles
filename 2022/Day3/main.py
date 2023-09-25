# Advent of Code - Day 3

dict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52
}


# Problem 1
# Determine the matching character in the first half of the rucksack with the
# second half of the rucksack.  Get the value of the character from the
# dictionary and add it to a running total.  Return the final total and print
# it out.

def Rucksacks():
    with open('input.txt', 'r') as file:
        total_value = 0

        Lines = file.readlines()

        for line in Lines:
            line = line.strip()
            num_chars = len(line)
            if num_chars % 2 == 1:
                num_chars -= 1
            string1 = line[0:int(num_chars / 2)]
            string2 = line[int(num_chars / 2):]

            same_letter = False

            for letter1 in string1:
                for letter2 in string2:
                    if letter1 == letter2:
                        same_letter = True
                        letter_value = dict.get(letter1)
                        total_value = total_value + letter_value
                        break
                if same_letter == True:
                    break

    return total_value


total = Rucksacks()
print(total)


# Problem 2
# Determine the item (character) that is the same in three consecutive rows
# of data.  Add the value of the item to the running total.  Go to the next
# three rows.  Return the final total and print.

def Rucksacks2():
    with open('input.txt', 'r') as file:
        total_value = 0

        i = 0

        Lines = file.readlines()

        for i in range(0, len(Lines), 3):
            line1 = Lines[i]
            line2 = Lines[i + 1]
            line3 = Lines[i + 2]

            same_letter = False

            for letter1 in line1:
                for letter2 in line2:
                    if letter1 == letter2:
                        for letter3 in line3:
                            if letter1 == letter3 and letter2 == letter3:
                                same_letter = True
                                letter_value = dict.get(letter1)
                                total_value = total_value + letter_value
                                break
                    if same_letter == True:
                        break
                if same_letter == True:
                    break

        return total_value


total = Rucksacks2()
print(total)
