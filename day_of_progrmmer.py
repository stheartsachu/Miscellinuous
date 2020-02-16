year = 1918
var = 0
if year == 1700 or year == 1800 or year == 1900 or year == 1918:
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        var = 31+29+31+30+31+30+31+31
        diff = 256-var-1
        if diff <= 31:
            print("%s.%s%s.%s" % (diff, 0, 9, year))
    elif year == 1918:
        print("26.09.1918")
    else:
        var = 31+28+31+30+31+30+31+31
        diff = 256-var-1
        if diff <= 31:
            print("%s.%s%s.%s" % (diff, 0, 9, year))
else:
    if year >= 1700 and year <= 1917:
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
    else:
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
