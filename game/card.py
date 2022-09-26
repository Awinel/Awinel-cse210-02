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
        self.card_num = random.randint(1, 13)
        self.last_card = 0

    def next_card(self):
        """Generates a random card from 1 to 13 to the dealer to show.
        """
        self.card_num = random.randint(1, 13)
        return self.card_num

    def shuffle(self):
        """This method keep the current card as last card."""

        self.last_card = self.card_num