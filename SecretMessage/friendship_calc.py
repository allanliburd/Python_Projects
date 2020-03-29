##
# show how compatible 2 people are by calculating a friendship score
##

friend_names = input("Please enter the names of 2 people: ")
score = 0
vowels = 'aeiou'
special = 'friend'

for character in friend_names:
    if character in vowels:
        score += 5
    else:
        score += 1
    if character in special:
        score += 10
    elif character in 'qvwxyz':
        score +=15
print("your friendship score is : ", score)

if score >= 85:
    print('Y\'all are Best Friends!')
elif score >= 65:
    print('Y\'all are Good Friends!')
elif score < 35:
    print('Y\'all are not good friends whatsoever...')
else:
    print('Y\'all are just friends.')