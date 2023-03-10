class DEALER:
    def __init__(self, deck):
        self.deck = deck
        self.hand = []
    
    def draw_card(self):
        print("Dealer: I'm drawing a card")
        return self.deck.pop(0)
    
    def initial_deal(self, player):
        # Deal two cards to the player and the dealer
        print("Dealer: Let's start, here are your cards")
        for _ in range(2):
            player.add_to_hand(self.draw_card())
            self.add_to_hand(self.draw_card())

    def add_to_hand(self, card):
        print("Dealer: Adding to my hand")
        self.hand.append(card)
        
    def add_to_hand(self, card):
        self.hand.append(card)
        
    def get_hand_value(self):
        # Calculate the value of the dealer's hand
        total = 0
        num_aces = 0
        
        # If the hand only has two cards (i.e. the initial deal), only consider the face-up card
        if len(self.hand) == 2:
            rank = self.hand[0][0]
            if rank.isdigit():
                total += int(rank)
            elif rank in ["J", "Q", "K"]:
                total += 10
            else:
                num_aces += 1
                total += 11
        else:
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
        
        
    def show_face_up_card(self):
        print("Dealer's face-up card: ", self.hand[0])
    
    def show_hand(self):
        # Show the hand that the player has
        print(f"Dealer's hand: {self.hand}")
        
    def is_bust(self):
        return self.get_hand_value() > 21
    
    def play(self):
        # The dealer must draw until they have at least 17 points
        print("I'm obligated to draw a card")
        while self.get_hand_value() < 17:
            self.add_to_hand(self.draw_card())
            
    def reset(self):
        self.hand = []

