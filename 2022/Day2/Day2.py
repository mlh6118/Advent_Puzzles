file2 = open('input.txt', 'r')

total_score = 0

while True:
    Line = file2.readline().strip()
    if len(Line) == 0:
        break
    Line = Line.split(' ')

    if Line[1] == 'X':
        total_score += 1
    elif Line[1] == 'Y':
        total_score += 2
    else:
        total_score += 3

    if Line[1] == 'X':
        if Line[0] == 'A':
            total_score += 3
        elif Line[0] == 'C':
            total_score += 6
    elif Line[1] == 'Y':
        if Line[0] == 'B':
            total_score += 3
        elif Line[0] == 'A':
            total_score += 6
    else: # Line[1] = 'Z'
        if Line[0] == 'C':
            total_score += 3
        elif Line[0] == 'B':
            total_score += 6

print(total_score)

file2.close()
