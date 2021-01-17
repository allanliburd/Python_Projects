import sys
import datetime
import time

# Test the above function
maxN = 12
minN = 3
count = 0

if len(sys.argv) > 1:
    maxN = int(sys.argv[1])
if len(sys.argv) > 2:
    minN = int(sys.argv[2])

print ("List all prime numbers from "+ str(minN) +" until "+ str(maxN) + ":\n")

pOut = open("prime_numbers.txt", 'r')
start = datetime.datetime.now()

numbers = pOut.readlines()
n = 3
count = 0

for line in numbers:
    for num in line:
        if num > maxN:
            break
        if num.isdigit() == True and num >= minN and num <= maxN:
            count += 1
        
end = datetime.datetime.now()
delta = (end -start).total_seconds() * 1000
msg = "Read " + str(count) + " prime numbers between "+ str(minN) +" and " + str(maxN) + " in " + str(delta) + " milliseconds"
print (msg)
pOut.close()

pOut = open("prime_numbers_BTY.txt", 'w')
pOut.write(msg + "\n")
pOut.close()
