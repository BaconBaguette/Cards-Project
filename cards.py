class Card(object):
	def __init__(self, name, description):
		self.name = name
		self.description = description

class Minion(Card):
	def __init__(self, name, description, attack, health, type):
		self.attack = attack
		self.health = health
		self.type = type
		super(Minion, self).__init__(name, description)

	def __repr__(self):
		return "%s \nAtt:%d  HP:%d" % (self.name, self.attack, self.health)
		
	def full_description(self):
		print "%s\nAttack:%d\nHealth:%d\n%s" % (self.name, self.attack, self.health, self.description)
		print


class Brute(Minion):
	def __init__(self):
		super(Brute, self).__init__("Brute", "Not as strong as he thinks he is.", 1, 4, "minion")

class Widowmaker(Minion):
	def __init__(self):
		super(Widowmaker, self).__init__("Widowmaker", "Hope you don't find out why they call her that.", 3, 1, "minion")

class Raptor_Man(Minion):
	def __init__(self):
		super(Raptor_Man, self).__init__("Raptor Man", "Really more of a raptor boy.", 2, 2, "minion")