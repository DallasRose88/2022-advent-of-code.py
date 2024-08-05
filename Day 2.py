f = open('trial.txt','r')

total = 0 

for line in f: 
    if line[0] == 'A':
        if line[2] == 'X':
            total += 3
        if line[2] == 'Y':
            total += 4
        if line[2] == 'Z':
            total += 8
    elif line[0] == 'B':
        if line[2] == 'X':
            total += 1
        if line[2] == 'Y':
            total += 5
        if line[2] == 'Z':
            total += 9
    elif line[0] == 'C':
        if line[2] == 'X':
            total += 2
        if line[2] == 'Y':
            total += 6
        if line[2] == 'Z':
            total += 7
print(total)
