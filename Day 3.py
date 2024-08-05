f = open('trial.txt','r')

total = 0
total2 = 0
for line in f:
    replace = line.replace(',','-').strip()
    split = replace.split('-')
    x = int(split[0])
    rooms = []
    while x < int(split[1])+1:
        rooms.append(x)
        x += 1 
    y = int(split[2])
    room2 = []
    while y < int(split[3]) +1:
        room2.append(y)
        y += 1 
    count = 0 
    count3 = 0
    for x in rooms:
        if x not in room2:
            count += 1 
        else:
            count3 += 1
    count2 = 0
    for y in room2:
        if y not in rooms:
            count2 += 1
    if count == 0 or count2 == 0:
        total += 1
    if count3 > 0:
        total2 += 1
print('Part 1', total)
print('Part 2', total2)
