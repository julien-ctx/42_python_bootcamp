from cmd import IDENTCHARS
import sys, subprocess

class Account(object):
	ID_COUNT = 1

	def __init__(self, name, **kwargs):
		self.__dict__.update(kwargs)
		self.id = self.ID_COUNT
		Account.ID_COUNT += 1
		self.name = name
		if not hasattr(self, 'value'):
			self.value = 0
		if self.value < 0:
			raise AttributeError("Attribute value cannot be negative.")
		if not isinstance(self.name, str):
			raise AttributeError("Attribute name must be a str object.")
		self.is_corrupted = False
		if not len(kwargs) % 2:
			self.is_corrupted = 1
		elif True in [x.startswith('b') for x in kwargs.keys()]:
			self.is_corrupted = 2
		elif not True in [(x.startswith('zip') or x.startswith('addr')) for x in kwargs.keys()]:
			self.is_corrupted = 3
		elif not hasattr(self, 'value') or not hasattr(self, 'id') or not hasattr(self, 'name'):	
			self.is_corrupted = 4
		elif not isinstance(self.name, str) or not isinstance(self.id, int) or not isinstance(self.value, (int, float)):
			self.is_corrupted = 5

	def transfer(self, amount):
		self.value += amount

	def newAttr(self, key, val):
		setattr(self, key, val)

class Bank(object):
	"""The bank"""
	def __init__(self):
		self.accounts = []
	
	def add(self, new_account):
		"""Add new_account in the Bank
		@new_account: Account() new account to append
		@return True if success, False if an error occured
		"""
		if not isinstance(new_account, Account):
			print("Error: cannot an non-Account object to bank")
			return False
		for account in self.accounts:
			if new_account.name == account.name:
				print("Error: an account with the same name already exists!")
				return False
		self.accounts.append(new_account)
		return True

	def transfer(self, origin, dest, amount):
		"""" Perform the fund transfer
		@origin: str(name) of the first account
		@dest: str(name) of the destination account
		@amount: float(amount) amount to transfer
		@return True if success, False if an error occured
		"""
		origin_acc = None
		dest_acc = None
		for account in self.accounts:
			if origin == account.name:
				origin_acc = account
			if dest == account.name:
				dest_acc = account
		if not origin_acc or not dest_acc:
			print(f"Error: cannot transfer from {origin} to {dest}. Check account names!")
			return False
		if origin_acc.is_corrupted or dest_acc.is_corrupted:
			return False
		if origin != dest:
			if amount < 0 or origin_acc.value - amount < 0:
				print("Error: current value of one of both accounts doesn't allow this transfer")
				return False
			origin_acc.value -= amount
			dest_acc.transfer(amount)
		print(f"Successfully transfered {amount} from {origin} to {dest}")
		return True

	def fix_account(self, name):
		""" fix account associated to name if corrupted
		@name: str(name) of the account
		@return True if success, False if an error occured
		"""
		if not isinstance(name, str):
			return False
		for curr_account in self.accounts:
			if name == curr_account.name:
				if curr_account.is_corrupted == 1:
					curr_account.newAttr("State", "OK")
				elif curr_account.is_corrupted == 2:
					for key in curr_account.__dict__.keys():
						if key.startswith('b'):
							key.replace('b', '')
				elif curr_account.is_corrupted == 3:
					curr_account.newAttr("zip", "Default")
				elif curr_account.is_corrupted == 4:
					curr_account.newAttr("name", "Default")
					curr_account.newAttr("id", Account.ID_COUNT + 1)
					Account.ID_COUNT += 1
					curr_account.newAttr("value", 0)
				elif curr_account.is_corrupted == 5:
					curr_account.name = "Default"
					curr_account.id = Account.ID_COUNT + 1
					curr_account.value = 0
				curr_account.is_corrupted = False
				return True
		else:
			return False
