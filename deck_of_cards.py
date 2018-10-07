class Cards:
	def __init__(self,suit,value):
		self.suit=suit
		self.value=value

	@classmethod
	def __repr__(cls):
		return("{} of {}".format(self.value,self.suit))
	@classmethod
	def bulk_cards(cls,data_suit,data_value):
		return cls(data_suit,data_value)
class Deck:
	suits=["Hearts","Diamonds","Clubs","Spades"]
	values=["A","2","3","4","5","6","7",
	"8","9","10","J","Q","K"]
