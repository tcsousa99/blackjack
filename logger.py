#A class responsable for logging messages to the terminal


class LOGGER:
    def __init__(self, verbose):
        self.verbose = verbose
    
    def PrintWelcome(self, players):
        if self.verbose >= 1:
            player_names = ', '.join([player.name for player in players])
            print(f"Welcome, {player_names}!")
    
    def PrintGoodbye(self, player):
        if self.verbose >= 1:
            print(f"Thank you for playing {player.name}, your total balance is {player.total_balance()}")

    def PrintNoMoney(self, player):
        if self.verbose >= 1:
            print(f"{player.name}, you don't have enough money! Introduce a new bet.")

    
    def PrintDeal(self, player):
        if self.verbose >= 2:
            print(f"Dealing cards to {player.name}...")
    
    def PrintHit(self, player):
        if self.verbose >= 2:
            print(f"{player.name} hits!")
    
    def PrintStand(self, player):
        if self.verbose >= 2:
            print(f"{player.name} stands!")
    
    def PrintBust(self, player):
        if self.verbose >= 2:
            print(f"{player.name} busts!")
    
    def PrintWin(self, player):
        if self.verbose >= 1:
            print(f"{player.name} wins!")
    
    def PrintLose(self, player):
        if self.verbose >= 1:
            print(f"{player.name} loses!")
    
    def PrintPush(self, player):
        if self.verbose >= 1:
            print(f"{player.name} pushed!")
    
    def PrintGameOver(self, player):
        if self.verbose >= 1:
            print(f"Game over! {player.name} has run out of money.")
    
    def PrintPlayerBalance(self, player):
        if self.verbose >= 1:
            print(f"{player.name} has a balance of {player.stack}.")
    
    def PrintDealerCards(self, dealer):
        if self.verbose >= 2:
            print("Dealer's cards:")
            dealer.show_hand()
    
    def PrintPlayerCards(self, player):
        if self.verbose >= 2:
            print(f"{player.name}'s cards:")
            player.show_hand()
    
    def PrintSeparator(self):
        if self.verbose >= 2:
            print("----------------")
