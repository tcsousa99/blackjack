import random

def generate_deck(seed):
    # Define the card suits and ranks
    suits = ["S", "H", "D", "C"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    
    # Set the random seed
    random.seed(seed)
    
    # Generate the deck by combining the suits and ranks
    deck = [(rank, suit) for suit in suits for rank in ranks]
    
    # Shuffle the deck randomly
    random.shuffle(deck)
    
    return deck



def card_value(card:tuple):
    value = 0
    
    rank = card[0]
    
    
    try:
        valor = int(card[0])
    except ValueError:
        if card[0] in ['Q', 'J', 'K']:
            valor = 10
        else:
            valor = 11
    return valor

D = generate_deck(3)



