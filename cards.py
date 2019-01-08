class Card(object):
	def __init__(self, name, description):
		self.name = name
		self.description = description
		
	def reset_card(self):
		self.__init__()

class Minion(Card):
	def __init__(self, name, description, attack, health, type):
		self.attack = attack
		self.health = health
		self.type = type
		super(Minion, self).__init__(name, description)

	def __repr__(self):
		return "%s \nAtt:%d  HP:%d" % (self.name, self.attack, self.health)


class Brute(Minion):
	def __init__(self):
		super(Brute, self).__init__("Brute", "Not as strong as he thinks he is.", 1, 4, "minion")

class C_B(Minion):
	def __init__(self):
		super(C_B, self).__init__("Cheeto Bandito", "Sniff my fingers.", 3, 1, "minion")

class Raptor_Man(Minion):
	def __init__(self):
		super(Raptor_Man, self).__init__("Raptor Man", "Really more of a raptor boy.", 2, 2, "minion")