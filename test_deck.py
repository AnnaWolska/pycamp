from deck import Deck

def test_creation():
    my_deck = Deck()
    assert len(my_deck.cards) == 52