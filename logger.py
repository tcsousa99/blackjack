#A class responsable for logging messages to the terminal

class LOGGER:
    def __init__(self):
        pass
    
    def PrintWin(self):
        print("You've won!")
        
    def PrintLose(self):
        print("You' lost!")
        
    def PrintNoMoney(self, player):
        print(f"{player.name}, you don't have enough money! Introduce a new bet.")
        
    def PrintPlayerHandValue(self, player):
        print(f"{player.name} hand has a value of", player.get_hand_value())
    
    def PrintPlayerHandValue(self, dealer):
        print(f"Dealers hand has a value of", dealer.get_hand_value())

    def InputAction(self, player):
        action = input(f"{player.name}, do you want to stand or hit? ")
        
