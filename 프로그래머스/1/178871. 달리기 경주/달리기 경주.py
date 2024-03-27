def solution(players, callings):
    i_dict = { p : i for i, p in enumerate(players) }
    
    for c in callings:
        i = i_dict[c]
        t = players[i - 1]
        
        players[i - 1] = players[i]
        players[i] = t
        
        i_dict[c] = i - 1
        i_dict[t] = i
        
    return players