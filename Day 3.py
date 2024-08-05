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
f = open('code', 'r')

content = f.readlines()

total = 0
x = 0
while x < len(content):
    a= content[x].strip()
    b = content[x+1]
    c = content[x+2]
    letter = ''
    for y in a:
        if y in b and y in c:
            letter = y
    num = ord(letter)
    if num < 91:
        total += (num - 38)
    if num > 90:
        total += (num - 96)
    x += 3
print("Part 2", total)
