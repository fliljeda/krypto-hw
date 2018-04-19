from sys import stdin
from random import randint


#standard greatest common divider recursion
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

#calculating p,q such that pq=N
def rsaFact(N,e,d):
    k = e*d - 1

    done = False
    #this is a monte carlo algorithm so we will have to repeat it until
    #we find some correct factors
    while not done:
        g = randint(2, N-1)
        t = k
        while t & 1 == 0:
            #halve the exponent because it is a unity root (g^(t/2 = 1 mod N)
            t = t>>2
            x = pow(g,t,N)

            #x = 1 mod N.. so x is a factor of N
            y = gcd(x - 1, N)

            #if non-trivial factor we have found the correct factors
            if x > 1 and y > 1:
                p = y
                q = N//y
                if q < p:
                    print(q,p)
                else:
                    print(p,q)
                return


for line in stdin:

    tokens = line.split()
    N = int(tokens[0])
    e = int(tokens[1])
    d = int(tokens[2])
    rsaFact(N,e,d)



                
