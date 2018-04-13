from sys import stdin

for line in stdin:
    tokens = line.split()
    a = int(tokens[0])
    e = int(tokens[1])
    n = int(tokens[2])

    val = 1
    while e > 0:
        #If uneven exponent: normal multiply
        if e & 1: 
            val = (a * val)%n

        #floor division by 2 because exponent is even at this point
        e = e >> 1 

        #square integer to accomodate for halving the exponent
        a = (a*a)%n
    print(val)
