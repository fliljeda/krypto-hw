from sys import stdin


for line in stdin:
    tokens = line.split()
    numofEqs = int(tokens[0])
    moduli = tokens[1:numofEqs+1]
    integers = tokens[numofEqs+1:]


    #compute product of all modulis
    N = 1
    for n in moduli:
        N *= int(n)

    y = [0]*len(moduli)
    #each y_i = N/n_i to ensure that once as a factor it becomes 0...  e.g  a * n_i %n_i
    for i,n in enumerate(moduli):
        y[i] = N/int(n)

    #compute inverse z for each y so a*y*z = a
    

def extended_gcd(a, b):
    s = 0
    old_s = 1
    t = 1
    old_t = 0
    r = b
    old_r = a
    while r != 0:
        q = old_r / r

