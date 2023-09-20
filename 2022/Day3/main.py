# Advent of Code - Day 3, Problem 1
# 1. Create function.
# 1a. Create loop.
# 2. Determine number of characters in rucksack.
# 3. Split string into two equal strings. (Ever uneven number?)
# 4. Loop through first string and check if character in second string.
# 5. Return duplicated letter.
# 6. Get value of letter from dictionary and add to total sum.
# 7. Print total sum. (for checking)
# 8. Return total sum.

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

def Rucksacks():

  with open('input.txt', 'r') as file:
    total_value = 0

    Lines = file.readlines()

    for line in Lines:
      line = line.strip()
      print(line)
      num_chars = len(line)
      print(num_chars)
      if num_chars % 2 == 1:
        num_chars -= 1
      string1 = line[0:int(num_chars / 2)]
      string2 = line[int(num_chars / 2 ):]

      same_letter = False
      
      for letter1 in string1:
        for letter2 in string2:
          if letter1 == letter2:
            same_letter = True
            letter_value = dict.get(letter1)
            total_value = total_value + letter_value
            print(total_value)
            break
        if same_letter == True:
          break
      
  return total_value

Rucksacks()
