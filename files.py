def createf(name):
    f = open(str(name), 'w')
    f.close()

def updatef(name, data):
    f = open(name, 'w')
    for i in data:
        s = ''
        s += str(i)
        s += ' '
        s += str(data[i])
        f.write(s + '\n')
    f.close()

def readf(name):
    data = {}
    f = open(name, 'r')
    for line in f:
        s = line.split(' ')
        data[str(s[0]).lower()] = int(s[1])
    return data
