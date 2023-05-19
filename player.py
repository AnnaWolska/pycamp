from cards import Card

class Player:
    def __init__(self):
        self.cards = []

    def take_card(self, card:Card):
        self.cards.append(card)
        print("1 self.cards", self.cards)

    def calculate_points(self):
        points = 0
        for card in self.cards:
            print("2 card",card)
            if card in ["Ace","Jack","Queen","King"]:
                points += 10
            else:
                points += int(card.value)
                print("3 card.value",card.value)
        return points

    some_card = Card(5,"hearts")
    print("4 some_card",some_card)
    print("5 some_card.color, some_card.value", some_card.value, some_card.color )
