f = open('trial.txt', 'r')

tots = []
count = 0 

for line in f:
    x = line.strip()
    if x.isdigit():
        count += int(line)
    else:
        tots.append(count)
        count = 0 
print('part1',max(tots))
top_three = 0
x = 0
while x < 3:
    a = max(tots)
    top_three += a
    b = tots.index(a)
    tots[b] = 0
    x += 1 
print('Part 2',top_three)
