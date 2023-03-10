#Class for the blackjack player. It contains his/her name as well as the initial money their willing to start with (buy_in) and the amount they have at the moment called stack.


class PLAYER:

    numb_of_players = 0
    name_of_players = []
    
    def __init__(self, name, buy_in):
        self.name = name
        self.buy_in = buy_in
        self.stack = buy_in
        self.bet = 0
        self.hand = []
        
        PLAYER.numb_of_players += 1
        PLAYER.name_of_players.append(name)
    
    #Total balance. Is the player gaining or losing money since he/her started?
    def total_balance(self):
        return self.stack - self.buy_in

    def add_to_stack(self, amount):
        self.stack += amount

    def remove_from_stack(self, amount):
        self.stack -= amount
        
    def win(self):
        print("You've won!")
        self.add_to_stack(self.bet)
    
    def lose(self):
        # If the player loses to the dealer then the amount they 
        print("You've lost!")
        self.remove_from_stack(self.bet)
        
        
    def push(self):
        # When both dealer and player tie
        self.add_to_stack(self.bet)
        self.bet = 0
        
    def add_to_hand(self, card):
        self.hand.append(card)    
        
    def show_hand(self):
        # Show the hand that the player has
        print(f"{self.name}'s hand: {self.hand}")
        
        
    def get_hand_value(self):
        # Calculate the value of the player's hand
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
        
    def is_bust(self):
        return self.get_hand_value() > 21
    
    def bust(self):
        self.lose()
        self.bet = 0
        self.hand = []
        print(f"{self.name} is bust!")
        
    def place_bet(self, amount):
        self.bet = amount
                
    def reset(self):
        self.hand = []
        self.bet = 0






