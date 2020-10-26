foundCounts = {}


def collatzSequence(start):
    next = start
    count = 0
    while(next != 1):


        if next in foundCounts:
            count += foundCounts[next]
            break
        else:
            count += 1
            if(next % 2):
                next = 3 * next + 1
            else:
                next = next /2


    if not start in foundCounts:
        # print(start, count)
        foundCounts[start] = count



    return count +1

maxCollatzNumber, maxCollatzLength = 0, 0

for i in range(1, 1000000):
    collatzChainLength = collatzSequence(i)
    if(collatzChainLength > maxCollatzLength):
        maxCollatzNumber, maxCollatzLength = i, collatzChainLength
        print(maxCollatzNumber, maxCollatzLength)


print(maxCollatzNumber, maxCollatzLength)


# def collatzsequence(largest):
#     maxchain = 0
#     for numbers in range(1,largest+1):
#         chainlength = 0
#         startingnumber = numbers
#         while numbers != 1:
#             if numbers % 2 == 0:
#                 numbers = numbers / 2
#                 chainlength +=1
#             else:
#                 numbers =numbers *3 + 1
#                 chainlength +=1
#         else:
#             chainlength +=1
#             if chainlength > maxchain:
#                 print(startingnumber,chainlength)
#                 maxchain=chainlength
#
#
#
# collatzsequence(1000000)

