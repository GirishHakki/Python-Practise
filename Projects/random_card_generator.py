import random
cards = ["Spades", "Clubs", "Diamond", "Hearts"]

ranks = [1,2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]

def rand_card():
    random_cards=random.choice(cards)
    random_ranks=random.choice(ranks)

    print(f"The [{random_cards}] of [{random_ranks}]")

rand_card()