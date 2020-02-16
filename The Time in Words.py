h = 1
m = 1
time = ["one","two","three","four","five","six","seven","eight","nine","ten",
        "eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen",
        "eighteen","nineteen","twenty","twenty one"," twenty three","twenty four",
        "twenty five","twenty six"," twenty seven","twenty eight","twenty nine"]

hour = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,
        16,17,18,19,20,21,22,23,24,25,26,27,28,29]
# for i in range(len(time)):
#     print(hour[i])

n_h = int(h)
if m == 00:
    for i in range(len(time)):
        if hour[i] == n_h:
            print("%s o' clock" % time[i])

if m <= 30:
    if m == 15:
        for i in range(len(time)):
            if hour[i] == n_h:
                print("quarter past %s" % time[i])

    elif m == 30:
        for i in range(len(time)):
            if hour[i] == n_h:
                print("half past %s" % time[i])
    else:
        hr = ""
        mint = ""
        for i in range(len(time)):
            n_m = int(m)-1
            # print(hour[n_m])
            if hour[i] == n_m:
                mint = time[i]
                print(mint)
        for i in range(len(time)):
            if hour[i] == n_h:
                hr = time[i]
        print("%s minutes past %s" % (mint, hr))

if m > 30:

    r_m = int(abs(60-m))
    n_h_1 = h+1
    if m == 45:
        for i in range(len(time)):
            if hour[i] == n_h_1:
                print("quarter to %s" % time[i])
    else:
        hr1 = ""
        mint_1 = ""
        for i in range(len(time)):
            if hour[i] == n_h_1:
                hr1 = time[i]
        for i in range(len(time)):
            if hour[i] == r_m:
                mint_1 = time[i]

        print("%s minutes to %s" % (mint_1, hr1))
