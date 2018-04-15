from sys import stdin


#Returns 1 if given elliptic curve is singular and 0 if it is non-singular
def isSingular(p, a, b):
    #Using the descriminant -16(4a^3 + 27b^2) to determine if it is singular
    #found on https://en.wikipedia.org/wiki/Elliptic_curve
    return int((-16*(4*pow(a,3) + 27*pow(b,2)) % p) == 0)

#Returns the number of affine points in the given elliptic curve
#using a shortcut version of the naive approach
def affinePoints(p, a, b):
    points = 0
    residues = [0] * p

    #Storing the number of values that result in each quadratic residue 
    #for x-values in the array
    for x in range(p):
        residue = pow(x,2) % p
        residues[residue] += 1

    #Looping through all x's and adding the number of points
    #that can satisfy the elliptic curve equation by check the number
    #of quadratic residues that originated from a specific value
    for x in range(p):
        points += residues[(pow(x,3) + a*x + b) % p]
        
    return points


for line in stdin:
    tokens = line.split() #Tokenize line

    singular = isSingular(int(tokens[0]), int(tokens[1]), int(tokens[2]))
    points = affinePoints(int(tokens[0]), int(tokens[1]), int(tokens[2]))

    print(singular, points)


