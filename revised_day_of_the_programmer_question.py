year = 1918

def year_check1(year):
    if year % 400 or year % 4 == 0 and year % 100 != 0:
        return True
    return False

def year_check2(year):
    if year % 4 == 0:
        return True
    else:
        return False

print(year_check1(year))
print(year_check2(year))

if year_check1(year) == True and year_check2(year) == True:
    if year % 400 or year % 4 == 0 and year % 100 != 0:
        var = 31+29+31+30+31+30+31+31
        diff = 256-var
        if diff <= 31:
            print("%s.%s%s.%s" % (diff, 0, 9, year))
    else:
        var = 31+28+31+30+31+30+31+31
        diff = 256-var
        if diff <= 31:
            print("%s.%s%s.%s" % (diff, 0, 9, year))

if year_check1(year) == True and year_check2(year) == False:
    if year % 4 == 0:
        var = 31+29+31+30+31+30+31+31
        diff = 256-var
        if diff <= 31:
            print("%s.%s%s.%s" % (diff, 0, 9, year))
    else:
        var = 31+28+31+30+31+30+31+31
        diff = 256-var
        if diff <= 31:
            print("%s.%s%s.%s"%(diff,0,9,year))
