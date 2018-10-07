class Cards:
	def __init__(self,suit,value):
		self.suit=suit
		self.value=value
	def __repr__(cls):
		return("{} of {}".format(self.value,self.suit))
	@classmethod
	def bulk_cards(cls,data_suit,data_value):
		return cls(data_suit,data_value)
class Deck:
	suits=["Hearts","Diamonds","Clubs","Spades"]
	values=["A","2","3","4","5","6","7",
	"8","9","10","J","Q","K"]

	def __init__(self):
		self.caard=[]
		for st in Deck.suits:
			for st2 in Deck.values:
				self.caard.append(Cards.bulk_cards(st,st2))
	def __repr__(self):
		return ("Deck of {} card's".format(len(self.caard)))


deck1= Deck()

print(deck1)