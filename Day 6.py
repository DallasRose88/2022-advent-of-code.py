rejects = []  
x = 0 
while x < 4091:
    possible = []  
    possible.append(content[x])
    possible.append(content[x+1])
    possible.append(content[x+2])
    possible.append(content[x+3])
    possible.append(content[x+4])
    possible.append(content[x+5])
    possible.append(content[x+6])
    possible.append(content[x+7])
    possible.append(content[x+8])
    possible.append(content[x+9])
    possible.append(content[x+10])
    possible.append(content[x+11])
    possible.append(content[x+12])
    possible.append(content[x+13])
    check = set(possible)
    if len(check) == 14:
        break 
    else:
        rejects.append(content[x])
    x += 1
print(len(rejects)+14)
