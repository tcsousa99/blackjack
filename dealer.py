class DEALER:
    def __init__(self, deck):
        self.deck = deck
        self.hand = []
    
    def draw_card(self):
        return self.deck.pop(0)
    
    def initial_deal(self, player):
        # Deal two cards to the player and the dealer
        for _ in range(2):
            player.add_to_hand(self.draw_card())
            self.add_to_hand(self.draw_card())

    def add_to_hand(self, card):
        self.hand.append(card)
        
    def get_hand_value(self):
        # Calculate the value of the dealer's hand
        total = 0
        num_aces = 0
        
        for card in self.hand:
            rank = card[0]
            
            if rank.isdigit():
                total += int(rank)
            elif rank in ["J", "Q", "K"]:
                total += 10
            else:
                num_aces += 1
                total += 11
        
        # Adjust the value for aces
        while num_aces > 0 and total > 21:
            total -= 10
            num_aces -= 1
        
        return total
        
    def play(self):
        # The dealer must draw until they have at least 17 points
        while self.get_hand_value() < 17:
            self.add_to_hand(self.draw_card())