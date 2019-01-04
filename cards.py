class Card(object):
	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return self.name

class Minion(Card):
	def __init__(self, name, attack, health, description):
		self.name = name
		self.attack = attack
		self.health = health
		self.description = description
		self.summary = self.name + " , Att: " + str(self.attack) + " , HP: " + str(self.health)

	def __repr__(self):
		return " Name - %s \n Attack - %d \n Health - %d \n %s" % (self.name, self.attack, self.health, self.description)


brute_minion = Minion("Brute", 1, 4, "Not as strong as he thinks he is.")
raptor_man_minion = Minion("Raptor Man", 2, 2, "Really more of a raptor boy.")
widowmaker_minion = Minion("Widowmaker", 3, 1, "Hope you don't find out why they call her that.")