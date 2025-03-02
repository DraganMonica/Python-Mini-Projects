♠️ Blackjack Game

This is a console-based Blackjack game implemented in Python.  
The player competes against a computer dealer, trying to get a hand value closer to 21 without going over.


📂 Project Structure


- main.py: Contains the full logic for:
    - Dealing cards to player and computer.
    - Calculating hand scores.
    - Allowing the player to draw more cards or hold.
    - Applying Blackjack rules (aces counting as 1 or 11).
    - Comparing hands to determine the winner.


📝 Features

- ✅ Random card dealing from a deck (Ace counts as 1 or 11).
- ✅ Automatic handling of dealer behavior (draws until at least 17).
- ✅ Player decision to draw or hold.
- ✅ Full win/lose/draw logic based on Blackjack rules.
- ✅ Handles "Blackjack" (Ace + 10-value card on first two cards).


🚀 How to Run:

To play the game, run: main.py


🕹️ How to Play:

Both player and computer get 2 cards.
Player sees their cards and one of the dealer’s cards.
Player chooses:
y to draw another card.
n to hold.
Dealer automatically draws cards until reaching at least 17.
The game determines the winner based on standard Blackjack rules.
