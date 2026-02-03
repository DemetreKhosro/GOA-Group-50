# 4) შექმენი კლასი BankAccount: რომელსაც ექნება owner, balance, currency. შექმენი 2 ანგარიში და დაბეჭდე: რომელი ანგარიშია უფრო დიდი თანხით.

class BankAccount:
  def __init__(self, owner, balance, currency):
    self.owner = owner
    self.balance = balance
    self.currency = currency

account1 = BankAccount('john doe', 1350, 'USD')
account2 = BankAccount('david shavidze', 125, 'GEL')

balances = [account1.balance, account2.balance]

highest = balances[0]
for i in balances:
  if i > highest:
    highest = i
print(f"highest balance: {highest}")