# blackjack

A simple blackjack terminal game design to help users get better at blackjack with integrated probability hints on each hand!


## Next steps

1. Generate the baralhos in a random function.
2. Change the program so that classes are used instead of sequencial
   1. Player class: Name, buy-in, stack, bet and hand
   2. Dealer class: I'm still thinking if this is in fact just an instance of player where the buy-in is 0 and it has a very large amount of money
3. Have a function that generates random decks. Nevertheless that are different methods for the shuffling of cards looking at the response of chatGPT may help:
   > In most blackjack games, the cards are not shuffled after every hand. Instead, a portion of the deck (known as the "shoe") is used until it is depleted, and then the cards are shuffled and placed back in the shoe. The size of the shoe can vary depending on the casino or the specific game, but it is usually between 4 and 8 decks. By not shuffling the cards after every hand, the game can be played more quickly and with fewer interruptions. However, this also means that the remaining cards in the shoe can affect the probability of certain outcomes in the game, which can be advantageous or disadvantageous to the player depending on the situation. To prevent players from gaining an unfair advantage by tracking the cards that have been played, some casinos use a technique called "continuous shuffling" where the cards are shuffled continuously throughout the game. This can make it more difficult for players to track the cards and gain an advantage, but it can also increase the house edge and make it more difficult for skilled players to win.

4. A function that calculates the value of each card.