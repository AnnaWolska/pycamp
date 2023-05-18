"""BlackJAck Python game"""

class InvalidColor(Exception):
    """Exception when color is invalid"""
    pass

class InvalidValue(Exception):
    """Exception when value is invalid"""
    pass



class Card:
    """Card abstraction"""
    possible_colors = ["spades", "dimonds", "hearts", "clubs"]
    possible_values = list(range(2,11)) + ["Ace","Jack","Queen","King"]
    def __init__(self, value, color):

        if color not in self.possible_colors:
            raise  InvalidColor("Invalid color!")
        self.color = self.possible_colors

        if value not in self.possible_values:
            raise  InvalidValue("Invalid value!")
        self.value = self.possible_values

    def __repr__(self):
        return f'{self.value},{self.color}'


    # def __str__(self):

# class Deck():
#     def __init__(self, cards, owner):
#         self.cards = cards
#         self.owner = owner
#
# class Player():
#     def __init__(self, deck):
#         self.deck = deck
#
# class Crupier():
#     def __init__(self, deck):
#         self.deck = deck


some_card = Card(8, "hearts")
print(some_card.color, some_card.value)
