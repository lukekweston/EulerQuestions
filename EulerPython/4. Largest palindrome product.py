
def palindrome():

    max = 0

    for i in range(1000, 0, -1):
        for j in range(1000, 0, -1):
            if i * j > max and str(i * j) == str(i * j)[::-1]:
                max = i * j
    return max

print(palindrome())