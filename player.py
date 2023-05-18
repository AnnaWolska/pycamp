class Player:
    def __init__(self):
        self.cards = []

    def take_card(self, card:Card):
        self.cards.append(Card)

    def calculate_points(self):
        points = 0
        for card in self.cards:
            if card in ["Ace","Jack","Queen","King"]:
                points += 10
            else:
                points += card
        return points

