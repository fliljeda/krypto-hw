from sys import stdin


for line in stdin:
    tokens = line.split()
    numofmod = int(tokens[0])
    coprimes = tokens[1:numofmod+1]
    integers = tokens[numofmod+1:]
