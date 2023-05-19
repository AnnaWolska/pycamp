from cards import Card, InvalidColor, InvalidValue
import pytest


def test_creation():
    card = Card(3,"hearts")
    assert card.value == 3
    assert card.color == "hearts"


def test_creation_wrong_value():
    """Test if code raises exception when wrong value"""
    with pytest.raises(InvalidValue) as message:
        card = Card(99, "hearts")
        assert message == "Invalid card value!"

def test_creation_wrong_color():
    """Test if code raises exception when wrong color"""
    with pytest.raises(InvalidColor) as message:
        card = Card(3, "black")
        assert message == "Invalid card color!"

def test_card_representation():
    """Test if card has correct card representation"""
    assert repr(Card("Ace","hearts")) == "Ace,hearts"