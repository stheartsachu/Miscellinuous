year = 2100
def fun(year):
    if year % 4 == 0 and year % 400 != 0 and year % :
        return True


print(fun(year))

if fun(year) == True:
    if year % 400 == 0:
        var = 31+29+31+30+31+30+31+31
        diff = 256-var
        if diff <= 31:
            print("%s.%s%s.%s" % (diff, 0, 9, year))
    else:
        var = 31+29+31+30+31+30+31+31
        diff = 256-var
        if diff <= 31:
            print("%s.%s%s.%s" % (diff, 0, 9, year))
if fun(year) == None:

    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        var = 31+29+31+30+31+30+31+31
        diff = 256-var
        if diff <= 31:
            print("%s.%s%s.%s" % (diff, 0, 9, year))
    else:
        var = 31+28+31+30+31+30+31+31
        diff = 256-var
        if diff <= 31:
            print("%s.%s%s.%s" % (diff, 0, 9, year))
