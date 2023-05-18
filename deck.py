from cards import Card

class Deck:
    def __init__(self):

        self.cards = []
        for color in Card.possible_colors:
            for value in Card.possible_values:
                # print(color,value)
                self.cards.append(
                    Card(color=color, value=value)
                )



deck = Deck()
print(deck)