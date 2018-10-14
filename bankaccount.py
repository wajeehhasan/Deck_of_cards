class BankAccount:
	def __init__(self,owner,balance=0):
		self._owner=owner
		self._balance=balance
	def deposit(self,bal):
		self._balance=self._balance+bal
		return self._balance
	def withdraw(self,bal):
		self._balance=self._balance-bal
		return self._balance



u1=BankAccount("wajeeh")
u2=BankAccount("Rafay")

print(u1.deposit(100))
print(u2.deposit(200))
print(u1.withdraw(50))
print(u2.withdraw(100))