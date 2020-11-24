


#2 pound
ways = 0
target = 200

rollingSumP2 = 0

for pound2 in range(0, 201, 200):
    sum = pound2
    if (sum > target):
        break
    if (sum == target):
        ways += 1
        break
    for pound1 in range(0, 201, 100):
        sum = pound1 + pound2
        if (sum > target):
            break
        if (sum == target):
            ways += 1
            break
        for p50 in range(0, 201, 50):
            sum = p50 + pound1 + pound2
            if (sum > target):
                break
            if (sum == target):
                ways += 1
                break
            for p20 in range(0, 201, 20):
                sum = p20 + p50 + pound1 + pound2
                if (sum > target):
                    break
                if (sum == target):
                    ways += 1
                    break
                for p10 in range(0, 201, 10):
                    sum = p10 + p20 + p50 + pound1 + pound2
                    if (sum > target):
                        break
                    if (sum == target):
                        ways += 1
                        break
                    for p5 in range(0, 201, 5):
                        sum = p5 + p10 + p20 + p50 + pound1 + pound2
                        if (sum > target):
                            break
                        if (sum == target):
                            ways += 1
                            break
                        for p2 in range(0, 201, 2):
                            sum = p2 + p5 + p10 + p20 + p50 + pound1 + pound2
                            if (sum > target):
                                break
                            if (sum == target):
                                ways += 1
                                break
                            for p1 in range(0, 201, 1):
                                sum = p1 + p2 + p5 + p10 + p20 + p50 + pound1 + pound2
                                if(sum > target):
                                    break
                                if(sum == target):
                                    ways+=1
                                    break

print(ways)
