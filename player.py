import cards
from cards import *


class Player(object):
	def __init__(self):
		self.cards_in_hand = []
		self.health = 30
		self.card_in_play = ''
		
		"""Returns true if the player has more than 0 health remaining
			Working"""
	def is_alive(self):
		return self.health > 0

		"""Adds the 3 cards currently in the game to the players hand
			Working"""
	def create_hand(self):
		self.cards_in_hand.append(Raptor_Man())
		self.cards_in_hand.append(Brute())
		self.cards_in_hand.append(Widowmaker())

		"""Prints to the console the cards currently in the players hand, or if empty, a statement telling them that.
			Currently prints in the format defined by the Minion class __repr__
			  Working"""
	def show_hand(self):
		if len(self.cards_in_hand)==0:
			print "You have no cards in hand."
		else:
			print "Cards in hand\n"
			for i in self.cards_in_hand:
				print i, "\n"
				
		"""Working, would like to find a better way to define cards in play, probably a 'Board' class"""
	def boardstate(self):
		for i in self.card_in_play:
			print "You have %s in play with %d health remaining" % (i.name, i.health)

		"""Minion in play attacks, hitting the opponents minion if there is one, or the opponent if not
			Working"""
	def minion_attack(self, opponent):
		if self.card_in_play == '':
			print "You don't have anything to attack with."
		elif opponent.card_in_play == '':
			opponent.health -= self.card_in_play.attack
			print "%s attacked opponent for %d damage. They have %d health remaining." % (self.card_in_play.name, self.card_in_play.attack, opponent.health)
		else:
			opponent.card_in_play.health -= self.card_in_play.attack
			if opponent.card_in_play.health <= 0:
				print "%s has attacked and killed opponents %s." % (self.card_in_play.name, opponent.card_in_play.name)
				opponent.card_in_play = ''
			else:
				print "%s attacked opponents %s for %d damage. %s has %d health remaining." % (self.card_in_play.name, opponent.card_in_play.name, self.card_in_play.attack, opponent.card_in_play.name, opponent.card_in_play.health)

class AI(object):
	def __init__(self):
		self.cards_in_hand = []
		self.health = 10
		self.card_in_play = Brute()

	def is_alive(self):
		return self.health > 0
		
	def create_hand(self):
		self.cards_in_hand.append(Raptor_Man())
		self.cards_in_hand.append(Brute())
		self.cards_in_hand.append(Widowmaker())