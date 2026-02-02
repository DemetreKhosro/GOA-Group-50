# 2) შექმენი კლასი Phone, რომელსაც ექნება:brand, storage(GB), price შექმენი 2 ტელეეფონი და დაბეჭდე რომელის არის უფრო ძვირი (if და property-ების გამოყენებით)

class Phone:
  def __init__(self, brand, storage, price):
    self.brand = brand
    self.storage = storage
    self.price = price

phone1 = Phone('Samsung', 128, 499)
phone2 = Phone('Xiaomi', 256, 799)

if phone1.price > phone2.price:
  print('phone 1 is more expensive than phone 2')
elif phone1.price == phone2.price:
  print('prices are equal')
else:
  print('phone 2 is more expensive than phone 1')