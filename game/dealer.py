

from cse210-02.game.card import Card


class Dealer:
    """The person who directs the game, ask hi/low about the game and shows the cards por the player.
    
    The responsability of Dealer is to ask the user a higher or lower card, keep score, deal cards
    and prompt the player if want keep playing.
    
    Attributes:
        card (list[Card]): A list of the possible cards to display.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score of the current game.
    """
    def __init__(self):
        """Create an instance of Dealer"""
        self.points = 300
        self.card = Card()

    def is_playing(self):
        """This method run the game logic"""
        
        while self.game_over() != True:
            print(f"The card is {self.card.card_num}")
            self.card.shuffle()
            self.hilo = input("Higher or lower? [h/l] ")
            print(f"Next card was: {self.card.next_card()}")
            if (self.card.card_num < self.card.last_card) and self.hilo == "l":
                self.points += 100
            elif (self.card.card_num > self.card.last_card) and self.hilo == "h":
                self.points += 100
            else:
                self.points -= 75
            print(f"Your score is :{self.points}")
            self.card.next_card()
            if self.points > 0:
                play_again = input("Play again? [y/n] ")
                if play_again.lower() != "y":
                    print("See you later")
                    break
        
    def game_over(self):
        """This method checks the points"""
        if self.points <= 0:
            print("Game over")
            return True
        else:
            return False