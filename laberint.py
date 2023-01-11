def readFile(fileName, sep=','):
    with open(fileName) as f:
        lines = f.readlines()
    return [tuple(map(int, line.split(sep))) for line in lines]


def findMaxWay(x, y, p, w):
    if x == rx-1 and y == ry-1:
        if p > resOne[0]:
            resOne[0] = p
            resOne[1] = w
    else:
        if x+1 < rx: 
            findMaxWay(x+1, y, p+ways[y][x+1], w + 'x')
        if y+1 < ry:
            findMaxWay(x, y+1, p+ways[y+1][x], w + 'y')


def findMinJumps(x, y, c, w):
    if x == rx-1 and y == ry-1:
        if c < resTwo[0]:
            resTwo[0] = c
            resTwo[1] = w
    else:
        if x+steps[y][x] < rx: 
            findMinJumps(x+steps[y][x], y, c + 1, w + f'x{steps[y][x]}')
        if y+steps[y][x] < ry:
            findMinJumps(x, y+steps[y][x], c + 1, w + 'y' + str(steps[y][x]))


ways = readFile('methods.csv')
steps = readFile('steps.csv')
resOne = [0, ""]
resTwo = [len(steps[0])**2, ""]
rx, ry = len(ways[0]), len(ways)
findMaxWay(0,0,ways[0][0], "")
print ("Задание №1\nМаксимальная длина: {0}, Путь: {1}".format(resOne[0], resOne[1]))
rx, ry = len(steps[0]), len(steps)
findMinJumps(0,0,0, "")
print ("Задание №2\nМинимальное кол-во шагов: {0}, Путь: {1}".format(resTwo[0], resTwo[1]))
