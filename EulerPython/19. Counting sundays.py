days = 365
sundayCount = 0

# Add 1 to days and check if its a sunday because or else it will be checking the last day of the previous month

for i in range(1,101):
    #jan
    if((days + 1) % 7 == 0):
        sundayCount += 1

    days += 31
    #feb
    if ((days + 1) % 7 == 0):
        sundayCount += 1

    if i % 4 == 0 or (i % 100 == 0 and i % 400 == 0):
        days += 29
    else:
        days += 28

    #march
    if ((days + 1) % 7 == 0):
        sundayCount += 1
    days += 31
    #april
    if ((days + 1) % 7 == 0):
        sundayCount += 1
    days += 30
    #may
    if ((days + 1) % 7 == 0):
        sundayCount += 1
    days += 31
    #june
    if ((days + 1) % 7 == 0):
        sundayCount += 1
    days += 30
    #july
    if ((days + 1) % 7 == 0):
        sundayCount += 1
    days += 31
    #august
    if ((days + 1) % 7 == 0):
        sundayCount += 1
    days += 31
    #sept
    if ((days + 1) % 7 == 0):
        sundayCount += 1
    days += 30
    #oct
    if ((days + 1)% 7 == 0):
        sundayCount += 1
    days += 31
    #nov
    if ((days + 1) % 7 == 0):
        sundayCount += 1
    days += 30
    #dec
    if ((days + 1) % 7 == 0):
        sundayCount += 1
    days += 31


print(days)
print(sundayCount)


