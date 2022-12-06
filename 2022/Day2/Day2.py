file2 = open('input.txt', 'r')

total_score = 0

while True:
    line = file2.readline().strip()
    if len(line) == 0:
        break
    line = line.split(' ')

    if line[1] == 'X':
        if line[0] == 'A':
            # Score Scissors losing to Rock
            total_score += 3
        elif line[0] == 'B':
            # Score Rock losing to Paper
            total_score += 1
        elif line[0] == 'C':
            # Score Paper losing to Scissors
            total_score += 2
    elif line[1] == 'Y':
        if line[0] == 'A':
            # Score Rock (1 + 3)
            total_score += 4
        elif line[0] == 'B':
            # Score Paper (2 + 3)
            total_score += 5
        elif line[0] == 'C':
            # Score Scissors (3 + 3)
            total_score += 6
    else:  # Line[1] = 'Z'
        if line[0] == 'A':
            # Score Paper win over Rock (2 + 6)
            total_score += 8
        elif line[0] == 'B':
            # Score Scissors win over Paper (3 + 6)
            total_score += 9
        elif line[0] == 'C':
            # Score Rock win over Scissors (1 + 6)
            total_score += 7

print(total_score)

file2.close()
