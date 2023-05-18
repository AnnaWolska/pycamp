from cards import Card
from random import shuffle

class Deck:
    def __init__(self):

        self.cards = []
        for color in Card.possible_colors:
            for value in Card.possible_values:
                print(color,value)
                self.cards.append(
                    Card(color=color, value=value)
                )
                print(self.cards)
                print(len(self.cards))

    def __repr__(self):
        return  f'{self.cards}'

    def shuffle(self):
        shuffle(self.cards)

    def hit(self):
        return self.cards.pop()


deck = Deck()
print(deck)


