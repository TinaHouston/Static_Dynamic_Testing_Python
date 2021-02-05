import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):

        self.game = CardGame("Game 1")
        self.card1 = Card("Spades", 1)
        self.card2 = Card("Hearts", 8)


    def test_has_ace(self):
        self.assertEqual(True, self.game.check_for_ace(self.card1))

    def test_highest_card(self):
        self.assertEqual(str(self.card2), self.game.highest_card(self.card1, self.card2))

    def test_cards_total(self):
        cards = [self.card1, self.card2]
        self.assertEqual("You have a total of 9", self.game.cards_total(cards))