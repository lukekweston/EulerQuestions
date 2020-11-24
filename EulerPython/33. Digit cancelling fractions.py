product = 1

# start at 11 to get rid of trivial answers
for n in range(11, 100):
    #increase denominator by 1 as it needs to be a fraction and not a whole number
    for d in range(n + 1, 100):
        # Check denokminator is not ending in 10, gets rid of more trivial answers
        if(d % 10 != 0):
            #check the value to be removed from the numerator and denominator is the same
            if(int(d / 10) == ( n % 10 )):
                #calculate n/d and n/d with the values removed and see if they are equal
                if( n/ d == int(n / 10) / ( d % 10 )):
                    print(n, "/", d)
                    print("%d / %d" % (int(n /10), (d %10)))
                    product *= (n/d)

print(round(1/product,0))