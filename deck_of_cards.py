class Cards:
	def __init__(self,suit,value):
		self.suit=suit
		self.value=value

	@classmethod
	def __repr__(cls):
		return("{} of {}".format(self.value,self.suit))
class Deck: