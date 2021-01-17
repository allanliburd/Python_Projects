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

    i = 2
    # This will loop from 2 to int(sqrt(x))
    while i*i <= n:
        # Check if i divides x without leaving a remainder
        if n % i == 0:
            # This means that n has a factor in between 2 and sqrt(n)
            # So it is not a prime number
            return False
        i += 1
    # If we did not find any factor in the above loop,
    # then n is a prime number
    return True

# Test the above function
maxN = 12
count = 0
if len(sys.argv) > 1:
    maxN = int(sys.argv[1])

print ("List all prime numbers from 3 until "+ str(maxN) + ":\n")

pOut = open("prime_numbers.txt", 'w')
start = datetime.datetime.now()

for x in range(3, maxN+1, 2):
    if (is_prime(x)):
        #print(x)
        pOut.write(str(x) + "\n")
        count += 1

end = datetime.datetime.now()
delta = (end -start).total_seconds() * 1000
msg = "Found " + str(count) + " prime numbers between 3 and " + str(maxN) + " in " + str(delta) + " milliseconds"
print (msg)
pOut.close()

pOut = open("prime_stats.txt", 'w')
pOut.write(msg + "\n")
pOut.close()