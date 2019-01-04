class Player(object):
	def __init__(self):
		self.cards_in_hand = []
		self.health = 30
		self.card_in_play = []
		
	def is_alive(self):
		return self.health > 0
		
	def create_hand(self):
		self.cards_in_hand.append(raptor_man_minion)
		self.cards_in_hand.append(brute_minion)
		self.cards_in_hand.append(widowmaker_minion)

	def show_hand(self):
		if len(self.cards_in_hand)==0:
			print "You have no cards in hand."
		else:
			print "Cards in hand\n"
			for i in self.cards_in_hand:
				print i, "\n"

	def show_hand_summ(self):
		if len(self.cards_in_hand)==0:
			print "You have no cards in hand."
		else:
			for i in self.cards_in_hand:
				print i.summary, "\n"

	def boardstate(self):
		print "You have %s in play with %d health remaining." % (self.card_in_play.name, self.card_in_play.health)


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
		self.card_in_play = widowmaker_minion

	def is_alive(self):
		return self.health > 0
		
	def create_hand(self):
		self.cards_in_hand.append(raptor_man_minion)
		self.cards_in_hand.append(brute_minion)
		self.cards_in_hand.append(widowmaker_minion)