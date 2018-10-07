class Cards:
	#
	def __init__(self,suit,value):
		self.suit=suit
		self.value=value
	#
	def __repr__(cls):
		return("{} of {}".format(cls.value,cls.suit))
	#class method
	@classmethod
	def bulk_cards(cls,data_suit,data_value):
		return cls(data_suit,data_value)
class Deck:
	#cards value
	suits=["Hearts","Diamonds","Clubs","Spades"]
	values=["A","2","3","4","5","6","7",
	"8","9","10","J","Q","K"]
	#
	def __init__(self):
		self.caard=[]
		for st in Deck.suits:
			for st2 in Deck.values:
				self.caard.append(Cards.bulk_cards(st,st2))
	#
	def __repr__(self):
		return ("Deck of {} card's".format(len(self.caard)))
	#
	def count(self):
		return "{} card's left".format(len(self.caard))
	#
	def _deal(self,number):
		self.dealed=[]
		if number<=len(self.caard):
			for x in range(0,number):
				self.dealed.append(self.caard.pop())
			return self.dealed
		if number>len(self.caard):
			for x in range(0,len(self.caard)):
				self.dealed.append(self.caard.pop())
		return self.dealed
		if len(self.caard)==0:
			raise ValueError "all cards have been dealt"

deck1= Deck()

print(deck1)
print(deck1.count())
print(deck1._deal(10))
print(deck1.count())