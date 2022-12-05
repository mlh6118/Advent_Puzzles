file2 = open('input.txt', 'r')

total_score = 0

while True:
    Line = file2.readline().strip()
    if len(Line) == 0:
        break
    Line = Line.split(' ')

    if Line[1] == 'X':
        if Line[0] == 'A':
            # Score Scissors losing to Rock
            total_score += 3
        elif Line[0] == 'B':
            # Score Rock losing to Paper
            total_score += 1
        elif Line[0] == 'C':
            # Score Paper losing to Scissors
            total_score += 2
    elif Line[1] == 'Y':
        if Line[0] == 'A':
            # Score Rock (1 + 3)
            total_score += 4
        elif Line[0] == 'B':
            # Score Paper (2 + 3)
            total_score += 5
        elif Line[0] == 'C':
            # Score Scissors (3 + 3)
            total_score += 6
    else:  # Line[1] = 'Z'
        if Line[0] == 'A':
            # Score Paper win over Rock (2 + 6)
            total_score += 8
        elif Line[0] == 'B':
            # Score Scissors win over Paper (3 + 6)
            total_score += 9
        elif Line[0] == 'C':
            # Score Rock win over Scissors (1 + 6)
            total_score += 7

print(total_score)

file2.close()
