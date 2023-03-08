#Class for the blackjack player. It contains his/her name as well as the initial money their willing to start with (buy_in) and the amount they have at the moment called stack.


class PLAYER:

    numb_of_players = 0
    name_of_players = []
    
    def __init__(self, name, buy_in,stack, bet, hand):
        self.name = name
        self.buy_in = buy_in
        self.stack = stack
        self.bet = bet
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
        
    def win(amount):
        print("You've won!")
        stack += amount
    
    def lose(amount):
        print("You've lost!")
        stack -= amount
        
    def push(self):
        self.add_to_stack(self.bet)
        self.bet = 0
        
    def show_hand(self):
        print(f"{self.name}'s hand: {self.hand}")
        
    def is_bust(self):
        hand_sum = sum(card_value(card) for card in self.hand)
        return hand_sum > 21
    
    def bust(self):
        self.lose(self.bet)
        self.bet = 0
        self.hand = []
        print(f"{self.name} is bust!")







