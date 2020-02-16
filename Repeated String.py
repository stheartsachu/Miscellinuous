s = "cfimaakj"
n =554045874191
if s.count("a") == 0:
    print(0)
else:
    if len(s) == 1:
        print(n)
    else:
        l = []
        i = 0
        break_point = 0
        while True:
            i += 1
            break_point += 1
            l.append(s[i-1])
            if i == len(s):
                i = 0
            if break_point == n:
                break
        print(l.count("a"))
