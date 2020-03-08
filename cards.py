# Assignment 08
# CSE-40028, 145020, Winter 2020
# Robert Dodson

class Card:
	def __init__(self, card_suit, card_value):
		self.card_suit = card_suit
		self.card_value = card_value

	def get_display_string(self):
		string_to_return = ""

		if self.card_value == 1:
			string_to_return = "Ace of "
		elif self.card_value == 2:
			string_to_return = "Two of "
		elif self.card_value == 3:
			string_to_return = "Three of "
		elif self.card_value == 4:
			string_to_return = "Four of "
		elif self.card_value == 5:
			string_to_return = "Five of "
		elif self.card_value == 6:
			string_to_return = "Six of "
		elif self.card_value == 7:
			string_to_return = "Seven of "
		elif self.card_value == 8:
			string_to_return = "Eight of "
		elif self.card_value == 9:
			string_to_return = "Nine of "
		elif self.card_value == 10:
			string_to_return = "Ten of "
		elif self.card_value == 11:
			string_to_return = "Jack of "
		elif self.card_value == 12:
			string_to_return = "Queen of "
		elif self.card_value == 13:
			string_to_return = "King of "

		if self.card_suit == 1:
			string_to_return += "Diamonds"
		elif self.card_suit == 2:
			string_to_return += "Hearts"
		elif self.card_suit == 3:
			string_to_return += "Spades"
		elif self.card_suit == 4:
			string_to_return += "Clubs"

		return string_to_return