VALID_CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
# 'Jack' == 10
# 'Queen' == 10
# 'King' == 10 

# def blackjack_score(hand):
#     score = 0
#     ace_value = 1

#     for card in hand:
#         if score < 11:
#             ace_value == 11
#             score += ace_value
#         # else:
#         #     ace_value == 1
#         #     score += ace_value

#         elif card in ['Jack', 'Queen', 'King']:
#             score += 10
#         else:
#             score += card

#     return score

# def blackjack_score(hand):
#     score = 0
#     for card in hand:
#         if card in ['Jack', 'Queen', 'King']:
#             score += 10
#         else:
#             score += card

#     return score

def blackjack_score(hand):
    score = 0
    ace_value = 11
    if len(hand) > 5:
         return "INVALID"

    for card in hand:
        if card not in VALID_CARDS:
            return "INVALID"
        else:
            if card == 'Ace':
                if score < 11:
                    ace_value = 11
                    score += ace_value
                else:
                    ace_value = 1
                    score += ace_value
            elif card in ['Jack', 'Queen', 'King']:
                    score += 10
            else:
                    score += card
    if score > 21:
        if "Ace" in hand:
            score = score - 10
        else:
            return 'BUST'

    return score

