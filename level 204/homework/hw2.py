# 2) შექმენი კლასი Product: რომელსაც ექნება name, price, quantity. შექმენი პროდუქტების სია და დაბეჭდე ყველაზე ძვირი და ყველაზე იაფი პროდუქტები

class Product:
  def __init__(self, name, price, quantity):
    self.name = name
    self.price = price
    self.quantity = quantity

product1 = Product('Apple', 5, 250)
product2 = Product('Milk', 8, 100)
product3 = Product('Pencil', 2, 200)
product4 = Product('Water', 1, 300)

prices = [product1.price, product2.price, product3.price, product4.price]

highest = prices[0]
for price in prices:
  if price > highest:
    highest = price
print(highest)
