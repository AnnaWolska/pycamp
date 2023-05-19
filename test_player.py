from player import Player
from cards import Card
# "Ace","Jack","Queen","King"

def test_calculate_player_points():
    #given
    card = Card(3,"hearts")
    card2 = Card(5,"spades")

    #when
    player = Player()
    player.take_card(card)
    player.take_card(card2)

    #then
    assert player.calculate_points()
