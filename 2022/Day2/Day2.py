file2 = open('input.txt', 'r')

total_score = 0

score_dict = {"A X": 3, "A Y": 4, "A Z": 8, "B X": 1, "B Y": 5, "B Z": 9,
              "C X": 2, "C Y": 6, "C Z": 7}

while True:
    line = file2.readline().strip()
    if not line:
        break
    total_score += score_dict[line]

print(total_score)

file2.close()
