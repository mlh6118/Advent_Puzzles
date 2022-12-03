file1 = open('input.txt', 'r')

elf_list = []
elf_total = 0
max_elf_total = 0

while True:
    Line = file1.readline()
    if len(Line) == 0:
        break
    Line = Line.strip()
    if Line == "":
        elf_list.append(elf_total)
        elf_total = 0
    else:
        elf_total += int(Line)

max_elf_total = max(elf_list)

print(max_elf_total)

file1.close()

# Part 2 addition
elf_list.sort(reverse=True)
top_3_elf_sum = elf_list[0] + elf_list[1] + elf_list[2]
print(top_3_elf_sum)
