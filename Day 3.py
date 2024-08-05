f = open('code', 'r')

total = 0
for line in f:
    a= len(line.strip())
    div = a //2
    one = line[:div]
    two = line[div:-1]
    letter = ''
    for x in one:
        if x in two:
            letter = x
    num = ord(letter)
    if num < 91:
        total += (num - 38)
    if num > 90:
        total += (num - 96)
print('Part 1', total)
#Part 2
