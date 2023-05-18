
class Card:
    possible_colors = ["spades", "dimonds", "hearts", "clubs"]
    possible_values = list(range(2,11)) + ["Ace","Jack","Queen","King"]
    def __init__(self, value, color):
        self.value = self.possible_values[value]
        self.color = self.possible_colors[color]

    # def __str__(self):

class Deck():
    def __init__(self, cards, owner):
        self.cards = cards
        self.owner = owner

class Player():
    def __init__(self, deck):
        self.deck = deck

class Crupier():
    def __init__(self, deck):
        self.deck = deck


# some_card = Card(8, "pik")
# print(some_card.color, some_card.number)




