

def time():
    s = "01:00:00AM"
    hour = "%s" % s[:2]
    minute = "%s" % s[3:5]
    second = "%s" % s[6:8]
    a = (s[-1])
    b = (s[-2])
    pahar = "%s%s" % (b, a)
    if pahar == "PM":
        if hour == "12":
            n_hour = '00'
            return "%s:%s:%s" % (n_hour, minute, second)

        if hour == "01":
            n_hour = "13"
            return "%s:%s:%s" % (n_hour, minute, second)

        if hour == "02":
            n_hour = "14"
            return "%s:%s:%s" % (n_hour, minute, second)

        if hour == "03":
            n_hour = "15"
            return "%s:%s:%s" % (n_hour, minute, second)

        if hour == "04":
            hour = "16"
            return "%s:%s:%s" % (hour, minute, second)

        if hour == "05":
            n_hour = "17"
            return "%s:%s:%s" % (n_hour, minute, second)

        if hour == "06":
            n_hour = "18"
            return "%s:%s:%s" % (n_hour, minute, second)

        if hour == "07":
            n_hour = "19"
            return "%s:%s:%s" % (n_hour, minute, second)

        if hour == "08":
            n_hour = "20"
            return "%s:%s:%s" % (n_hour, minute, second)

        if hour == "09":
            n_hour = "21"
            return "%s:%s:%s" % (n_hour, minute, second)

        if hour == "10":
            n_hour = "22"
            return "%s:%s:%s" % (n_hour, minute, second)

        if hour == "11":
            n_hour = "23"
            return "%s:%s:%s" % (n_hour, minute, second)

    if pahar == "AM":
        return "%s:%s:%s" % (hour, minute, second)

