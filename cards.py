def card(rank,suite):
    return {"rank": ranking(rank), "suite": suite, "value":rank}
    
    
def ranking(rank):
    match rank:
        case '14':
            return 'A'
        case '13':
            return 'K'
        case '12':
            return 'Q'
        case '11':
            return "J"
        case _:
             return rank
print(card('11', "H"))