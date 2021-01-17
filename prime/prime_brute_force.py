import sys
import datetime
import time

def is_prime(n):

    """
    Assumes that n is a positive natural number
    """
    # We know 1 is not a prime number
    if n == 1:
        return False

    # We store the number of factors in this variable
    factors = 0
    # This will loop from 1 to n
    for i in range(1, n+1):
        # Check if `i` divides `n`, if yes then we increment the factors
        if n % i == 0:
            factors += 1
    # If total factors are exactly 2
    if factors == 2:
        return True
    return False

# Test the above function
maxN = 12
count = 0
if len(sys.argv) > 1:
    maxN = int(sys.argv[1])
print ("List all prime numbers from 3 until "+ str(maxN) + ":\n")
start = datetime.datetime.now()
for x in range(3, maxN+1, 2):
    if (is_prime(x)):
        print( x)
        count += 1
end = datetime.datetime.now()
delta = (end -start).total_seconds() * 1000
print("Found " + str(count) + " prime numbers in " + str(delta) + " milliseconds")