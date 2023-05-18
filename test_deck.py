from deck import Deck
from cards import Card
from random import shuffle

def test_creation():
    my_deck = Deck()
    assert len(my_deck.cards) == 52

def test_deck():
    my_deck = Deck()
    cards = [(card.value, card.color) for card in my_deck.cards]

    for color in Card.possible_colors:
        cards_in_color = [card for card in cards if card[1] == color]
        assert len(cards_in_color) == 13

def test_shuffle():
    my_deck = Deck()
    cards = my_deck.cards[:]
    my_deck.shuffle()
    assert cards != my_deck.cards

def test_deck_hit():
    my_deck = Deck()
    last_card = my_deck.cards[-1]
    hitted_card = my_deck.hit()
    assert last_card == hitted_card