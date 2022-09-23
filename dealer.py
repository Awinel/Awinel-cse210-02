class Dealer:
    """The person who directs the game, ask hi/low about the game and shows the cards por the player.
    
    The responsability of Dealer is to ask the user a higher or lower card, keep score, deal cards
    and prompt the player if want keep playing.
    
    Attributes:
        card (list[Card]): A list of the possible cards to display.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score of the current game.
        """