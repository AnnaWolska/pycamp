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
    assert player.calculate_points() == 8

def test_calculate_player_points_two_aces():
    #given
    card = Card('Ace','spades')
    card2 = Card('Ace','hearts')

    #when
    player = Player()
    player.take_card(card)
    player.take_card(card2)

    #then
    assert player.calculate_points() == 21

def test_calculate_player_points_one_ace_two_cards():
    #given
    card = Card('Ace','spades')
    card2 = Card(2,'hearts')

    #when
    player = Player()
    player.take_card(card)
    player.take_card(card2)

    #then
    assert player.calculate_points() == 13

def test_calculate_player_points_three_cards():
    #given
    card = Card('Ace','spades')
    card2 = Card('Ace','hearts')
    card3 = Card('Ace','dimonds')

    #when
    player = Player()
    player.take_card(card)
    player.take_card(card2)
    player.take_card(card2)

    #then
    assert player.calculate_points() == 3