import math
def checkprime(primes, check):
    for i in primes:
        if i > math.sqrt(check):
            break
        if check % i == 0:
            return None

    return check

primer = []
number = 2
while len(primer) < 100:

    a = checkprime(primer,number)
    if not (a == None):
        primer.append(a)
    number += 1

print(primer)
