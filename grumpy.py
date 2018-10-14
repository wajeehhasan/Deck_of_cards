class grumpy(dict):
	def __repr__(self):
		return "NONE OF YOUR BUSINESS \n {}".format(self.dick)

	def __missing__(self,key):

	def __setitem__(self,key,value):
		print("god stop changing things")
		print("fine illll do it")
		super().__init(key,value)
	def __contains__(self,item):
		

d=grumpy({'d':'2'})
print(d)