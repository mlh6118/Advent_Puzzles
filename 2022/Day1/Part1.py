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
