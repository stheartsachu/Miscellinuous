p = 100  # cost of the first game
d = 19  # the amount that would we dectuted
m = 1 # last game price
s = 180 #  total amount you have ?
# 100 99 181 180
if s < p:
    print(0)
else:
    games = p
    games_list = []
    games_list.append(p)
    check = p
    games_counter = 0
    while True:
        games -= d
        check += games
        if check > s:
            break
        else:
            games_list.append(games)
            if games <= m:
                games_list.pop()
                games_list.append(m)
                break
    games_counter = len(games_list)
    t_s = s-sum(games_list)
    if t_s > m:
        val = games_list[-1]
        incrementer = s-t_s
        while True:
            incrementer += val
            games_counter += 1
            if incrementer == s:
                break
            if incrementer > s:
                games_counter -= 1
                break
    print(games_counter)
