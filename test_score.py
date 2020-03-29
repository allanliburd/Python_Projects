# Take a list of test scores and turn the scores
# into percentages before printing out the list

scores = [12, 5, 46, 32, 59]
total_mark = 50.0
percentages = []

i = 0

while i < 5:
    percent = round( (scores[i] / total_mark) * 100 )
    percentages.append( percent )
    i += 1

print(percentages)