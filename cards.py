class Card(object):
	def __init__(self, name, description):
		self.name = name
		self.description = description

class Minion(Card):
	def __init__(self, name, description, attack, health):
		self.attack = attack
		self.health = health
		super(Minion, self).__init__(name, description)

	def __repr__(self):
		return "%s \nAtt:%d  HP:%d\n%s" % (self.name, self.attack, self.health, self.description)


class Brute(Minion):
	def __init__(self):
		super(Brute, self).__init__("Brute", "Not as strong as he thinks he is.", 1, 4)

class Widowmaker(Minion):
	def __init__(self):
		super(Widowmaker, self).__init__("Widowmaker", "Hope you don't find out why they call her that.", 3, 1)

class Raptor_Man(Minion):
	def __init__(self):
		super(Raptor_Man, self).__init__("Raptor Man", "Really more of a raptor boy.", 2, 2)

This is a change I have made