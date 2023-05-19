from cards import Card

class Player:
    def __init__(self):
        self.cards = []

    def take_card(self, card:Card):
        self.cards.append(card)
        print("self.cards",self.cards)

    def calculate_points(self):
        points = 0
        for card in self.cards:
            print(card)
            if card in ["Ace","Jack","Queen","King"]:
                points += 10
            else:
                points += int(card.value)
                print("card.value",card.value)
        return points

    some_card = Card(5,"hearts")
    print("some_card",some_card)
    print(some_card.color, some_card.value)

    take_card(some_card)
    print("cards",cards)

    print(calculate_points(some_card))