with open ('22. names.txt') as f:
    # Sorts the names alphabetically
    names = sorted(f.read().replace('"','').split(","))
    position = 0
    totalScore = 0
    for name in names:
        position += 1
        score = 0
        for letter in name:
            score += (ord(letter) - ord('A')) + 1
        totalScore += score * position
    print(totalScore)

f.closed