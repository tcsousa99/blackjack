
#This defines the playability of a game, in this section each normal round should be
#played

from player import PLAYER
from dealer import DEALER
from logger import LOGGER
from functions import *


def play():
    #This could be changed to include more players
    name = str(input("Introduce your name: "))
    buy_in = float(input("Buy-in: "))
    #seed = random.randint(0, 50000)
    
    #Generate a deck
    seed = 2
    deck =  generate_deck(seed)
    player1 = PLAYER(name, buy_in)
    dealer = DEALER(deck)
    logger = LOGGER()
    
    #Game
    while True:
        #First, the player has to place a bet
        while True:
            try:
                bet = int(input(f"{player1.name}, enter your bet: "))
                if bet > player1.stack:
                    print(f"{player1.name}, you don't have enough money! Introduce a new bet.")
                    break
                else: 
                    player1.place_bet(bet)

            except ValueError:
                print("Invalid input, enter an integer")
        
        #Now the dealer must give two cards to each player and two to himself. 
        #One of the dealers cards must be visible and the player cards are all visible
            dealer.initial_deal(player1)
            player1.show_hand()
            dealer.show_face_up_card()

            print(f"{player1.name} hand has a value of", player1.get_hand_value())
            print(f"Dealers hand has a value of", dealer.get_hand_value())
            print("\n")
        #Now both player and dealer have cards. Now the player has the decision of
        #hitting or standing.
            while True:
                action = input(f"{player1.name}, do you want to stand or hit? ")
                action = logger.InputAction(player1)
                if action.lower() == "hit":
                    player1.add_to_hand(dealer.draw_card())
                    player1.show_hand()
                    if player1.is_bust():
                        print(f"{player1.name} hand has a value of", player1.get_hand_value())
                        player1.bust()
                        break
                    else:
                        print(f"{player1.name} hand has a value of", player1.get_hand_value())
                        
                elif action.lower() == "stand":
                    break
                
                else:
                    print("Invalid input: Please enter 'hit' or 'stand")
        
            #If the player did not bust, we continue to the next round, the dealer must show his
            #face-down card and then take another card until they have at least
            dealer.play()
            dealer.show_hand()
            print(f"Dealers hand has a value of", dealer.get_hand_value())

            
            dealer_value = dealer.get_hand_value()
            player_value = player1.get_hand_value()
            if player1.is_bust():
                pass
            elif dealer.is_bust():
                player1.win()
            elif player_value > dealer_value:
                player1.win()
            elif player_value < dealer_value:
                player1.lose()
            else:
                player1.push()
                
            print(f"{player1.name} has now {player1.stack} and started with {player1.buy_in}")

            #Check if the player wants to continue:
            while True:
                again = input(f"{player1.name}, do you want to play again? ")
                if again.lower() == "yes":
                    player1.reset()
                    dealer.reset()
                    seed = 3
                    deck =  generate_deck(seed)
                    break
                elif again.lower() == "no":
                    print(f"Thank you for playing {player1.name}, your total balance is {player1.total_balance()}")
                    return
                else:
                    print("Invalid input! Please enter 'yes' or 'no'.")
        

play()