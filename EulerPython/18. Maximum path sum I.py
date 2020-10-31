inputTriangle = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

def formatTriangle(inputTriangle):
    triangle = []
    for line in inputTriangle.split("\n"):
        lineList = []
        for n in line.split(" "):
            lineList.append(int(n))
        triangle.append(lineList)
    return triangle

####recursive brute force method startign from bottom -- slow
#gets all possible combinations going up
def getPath(triangle, row, path):
    #at the top of the triangle
    if row == 0:
        # print("hello", [0] + path)
        return [0] + path
    else:
        #can always only go to 0 on the next row if in 0 position
        if path[0] == 0:
            return getPath(triangle, row - 1, [0] + path)
        #can always only go to last positon if in last position
        elif path[0] == len(triangle[row]):
            return getPath(triangle, row - 1, [len(triangle[row]) - 1] + path)
        #compare numbers above and work out which path will create the greatest sum
        else:
            if sumPath(triangle, getPath(triangle, row - 1, [path[0]] + path)) > sumPath(triangle, getPath(triangle, row -1, [path[0] - 1] + path)):
                return getPath(triangle, row - 1, [path[0]] + path)
            else:
                return getPath(triangle, row -1, [path[0] - 1] + path)



def sumPath(triangle, path):
    sum = 0
    for i in range(len(path)):
        sum += triangle[i][path[i]]
    return sum

triangle = formatTriangle(inputTriangle)

lastRow = triangle[len(triangle) - 1]
sums = []
#
# #get the max values in every 2nd index for the last row (smaller ones dont need to be ever checked)
# for i in range(0, len(lastRow), 2):
#     path = []
#     if(i != len(lastRow) -1 and lastRow[i] < lastRow[i] + 1):
#         path = getPath(triangle, len(triangle) - 2, [i + 1])
#     else:
#         path = getPath(triangle, len(triangle) - 2, [i])
#
#
#     sums.append(sumPath(triangle,path))
#
# print("max path sum: ", max(sums))
# ###

def fastSum(triangle):
    trianglesSummed = triangle
    for row in range(len(triangle) - 2, -1, -1):
        for i in range(len(triangle[row])):
            if(trianglesSummed[row + 1][i] > trianglesSummed[row + 1][i + 1]):
                trianglesSummed[row][i] = trianglesSummed[row + 1][i] + triangle[row][i]
            else:
                trianglesSummed[row][i] = trianglesSummed[row + 1][i + 1] + triangle[row][i]
    return trianglesSummed[0]


print(fastSum(formatTriangle(inputTriangle)))



