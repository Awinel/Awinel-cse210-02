import random

class Card:
    """A pice of paper or plastic that have a number on it.

    The responsability of a Card is to keep a number between 1-13.
    
    Attributes:
        card_num (int): The number that is on the card"""
    
    def __init__(self):
        """Construct a new instance of Card.
        Arg:
            self (Card): An instance of card.
        """
        self.card_num = 0

    def suffle(self):
        """Generates a random card from 1 to 13 to the dealer to show.
        """
        self.card_num = random.randint(1, 13)
        return self.card_num

class Dealer:
    """The person who directs the game, ask hi/low about the game and shows the cards por the player.
    
    The responsability of Dealer is to ask the user a higher or lower card, keep score, deal cards
    and prompt the player if want keep playing.
    
    Attributes:
        card (list[Card]): A list of the possible cards to display.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score of the current game.
    """
    
        
    def get_inputs(self):
        """Ask the player for a higher or lower card."""
        card = Card()
        print(f"The card is {card.suffle()}")

dealer = Dealer()
dealer.get_inputs()