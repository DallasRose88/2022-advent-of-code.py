f = open('Trial2.txt','r')

total = 0
letters = []
for line in f:
    letter = ''
    a = (len(line.strip()))
    div = a//2
    first = line[0:div]
    second = line[div:]
    for x in first:
        if x in second:
            letter = x 
    num = ord(letter)
    if num > 90:
        num -=96
        total += num
    else:
        num -= 38
        total += num
print('part 1',total)
#Part 2
