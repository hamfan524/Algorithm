def solution(players, callings):
    player_dic = {}
    rank_dic = {}
    for i in range(len(players)):
        player_dic[players[i]] = i
        rank_dic[i] = players[i]

    for i in callings:
        rank = player_dic[i]
        player_dic[rank_dic[rank-1]], player_dic[rank_dic[rank]] = player_dic[rank_dic[rank]], player_dic[rank_dic[rank-1]]
        rank_dic[rank-1], rank_dic[rank] = rank_dic[rank], rank_dic[rank-1]
    
    for i in range(len(players)):
        players[i] = rank_dic[i]
    
    return players