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
# print(card('11', "H"))



def compare_cards(p1_card: dict, p2_card: dict) -> str:
    p1 = p1_card['value']
    p2 = p2_card['value']
    if p1 > p2: 
        return 'p1'
    elif p1 < p2: 
        return 'p2'
    return 'WAR'
print(compare_cards({"rank": "J", "suite": 'S', "value":11}, {"rank": "A", "suite": "A", "value":14}))