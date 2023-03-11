from player import PLAYER
from dealer import DEALER
from logger import LOGGER
from functions import *


def play():
    while True:
        try:
            num_players = int(input("Enter number of players: "))
            break
        except ValueError:
            print("Invalid input, enter an integer")
            

    players = []
    for i in range(num_players):
        name = str(input(f"Player {i+1}, introduce your name: "))
        buy_in = float(input("Buy-in: "))
        player = PLAYER(name, buy_in)
        players.append(player)
        
    seed = 2
    deck = generate_deck(seed)
    dealer = DEALER(deck)
    logger = LOGGER()
    round_counter = 0
    
    logger.PrintWelcome(players)
    
    while True:
        round_counter+=1
        logger.PrintRound(round_counter)
        for player in players:
            while True:
                try:
                    bet = int(input(f"{player.name}, enter your bet: "))
                    if bet > player.stack:
                        print(f"{player.name}, you don't have enough money! Introduce a new bet.")
                    else: 
                        player.place_bet(bet)
                        break
                except ValueError:
                    print("Invalid input, enter an integer")

            dealer.initial_deal(player)
            player.show_hand()
            dealer.show_face_up_card()

            logger.PrintPlayerHandValue(player)
            logger.PrintDealerHandValue(dealer)
            print("\n")

            while True:
                action = logger.InputAction(player)
                if action.lower() == "hit":
                    player.add_to_hand(dealer.draw_card())
                    player.show_hand()
                    if player.is_bust():
                        logger.PrintPlayerHandValue(player)
                        player.bust()
                        break
                    else:
                        logger.PrintPlayerHandValue(player)
                elif action.lower() == "stand":
                    break
                else:
                    print("Invalid input: Please enter 'hit' or 'stand")

            dealer.play()
            dealer.show_hand()
            logger.PrintDealerHandValue(dealer)

            dealer_value = dealer.get_hand_value()
            player_value = player.get_hand_value()
            if player.is_bust():
                pass
            elif dealer.is_bust():
                player.win()
            elif player_value > dealer_value:
                player.win()
            elif player_value < dealer_value:
                player.lose()
            else:
                player.push()
                
            print(f"{player.name} has now {player.stack} and started with {player.buy_in}")

        while True:
            again = input(f"Do you want to play again? ")
            if again.lower() == "yes":
                for player in players:
                    player.reset()
                dealer.reset()
                seed = 3
                deck = generate_deck(seed)
                break
            elif again.lower() == "no":
                for player in players:
                    logger.PrintGoodbye(player)
                    players.remove(player)
                return
            else:
                print("Invalid input! Please enter 'yes' or 'no'.")
        
play()
