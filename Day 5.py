f = open('trial.txt','r')

boxes = {1:['D','B','J','V'],2:['P','V','B','W','R','D','F'],3:['R','G','F','L','D','C','W','Q'],4:['W','J','P','M','L','N','D','B'],5:['H','N','B','P','C','S','Q'],6:['R','D','B','S','N','G'],7:['Z','B','P','M','Q','F','S','H'],8:['W','L','F'],9:['S','V','F','M','R']}


for line in f:
    split = line.strip().split(' ')
    old = int(split[3])
    new = int(split[5])
    x = 0
    while x < int(split[1]):
        letter = boxes[old][-1]
        boxes[old].pop()
        boxes[new].append(letter)
        x += 1

ends =[]
y = 1
while y < (len(boxes)+1):
    ends.append(boxes[y][-1])
    y += 1
print(ends)

#Part 2
f = open('trial.txt','r')

boxes = {1:['D','B','J','V'],2:['P','V','B','W','R','D','F'],3:['R','G','F','L','D','C','W','Q'],4:['W','J','P','M','L','N','D','B'],5:['H','N','B','P','C','S','Q'],6:['R','D','B','S','N','G'],7:['Z','B','P','M','Q','F','S','H'],8:['W','L','F'],9:['S','V','F','M','R']}


for line in f:
    split = line.strip().split(' ')
    old = int(split[3])
    new = int(split[5])
    x = int(split[1])
    while x > 0:
        letter = boxes[old][-x]
        boxes[old].pop(-x)
        boxes[new].append(letter)
        x -= 1

ends =[]
y = 1
while y < (len(boxes)+1):
    ends.append(boxes[y][-1])
    y += 1
print(ends)
