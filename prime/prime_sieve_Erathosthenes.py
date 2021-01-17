import sys
import datetime
import time

def sieve(N):
    """
    We cross out all composites from 2 to sqrt(N)
    """
    i = 2
    # This will loop from 2 to int(sqrt(x))
    while i*i <= N:
        global is_prime
        # If we already crossed out this number, then continue
        if is_prime[i] == 0:
            i += 1
            continue

        j = 2*i
        while j < N:
            # Cross out this as it is composite
            is_prime[j] = 0
            # j is incremented by i, because we want to cover all multiples of i
            j += i

        i += 1


maxN = 12
count = 0

# grab a maximum number from the command line
if len(sys.argv) > 1:
    if ("max" == sys.argv[1]):
        maxN = int(sys.maxsize/2 + 0.5)
        print("maxN = " + str(maxN))

    else:
        temp = int(sys.argv[1])
        if temp >= 0:
            maxN = temp

is_prime = [1] * maxN
is_prime[0] = maxN
is_prime[1] = 0

print ("List all prime numbers from 3 until "+ str(maxN) + ":\n")

start = datetime.datetime.now()
sieve(maxN)

for x in range(3, maxN+1, 2):
    if is_prime[x] == 1:
        print( x)
        count += 1

end = datetime.datetime.now()
delta = (end -start).total_seconds() * 1000

print("Found " + str(count) + " prime numbers in " + str(delta) + " milliseconds")
print("maxint = " + str(sys.maxsize))