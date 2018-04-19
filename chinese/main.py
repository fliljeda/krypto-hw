from sys import stdin

#extended euclidean algorithm
#found on https://brilliant.org/wiki/extended-euclidean-algorithm/
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return x

for line in stdin:
    tokens = line.split()
    numofEqs = int(tokens[0])
    moduli = tokens[1:numofEqs+1]
    integers = tokens[numofEqs+1:]


    #compute product of all modulis
    N = 1
    for n in moduli:
        N *= int(n)

    #each y_i = N/n_i so that all other integers is 0 under this moduli when this
    #is a factor
    y = [0]*numofEqs
    for i,n in enumerate(moduli):
        y[i] = N//int(n)

    #compute inverse z for each y so a*y*z = a to remove the effect each y has
    #on the integers
    z = [0]*numofEqs
    for i,n in enumerate(y):
        z[i] = egcd(y[i],int(moduli[i]))

    #an answer is found by adding the products of the integers, their respective
    #y and z. The unique answer is modulo N
    ans = 0
    for i in range(numofEqs):
        ans += int(integers[i]) * y[i]  * z[i] 
        ans = ans%N
    print(ans % N)
    
