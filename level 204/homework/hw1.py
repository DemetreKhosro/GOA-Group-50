# 1) შექმენი კლასი Player: რომელსაც ექნება name, score, level. შექმენი 3 მოთამაშე და დაბეჭდე: რომელი მოთამაშეა ყველაზე მაღალი score-ით

class Player:
  def __init__(self, name, score, level):
    self.name = name
    self.score = score
    self.level = level

player1 = Player('john', 85, 10)
player2 = Player('zangi', 67, 41)
player3 = Player('nick', 50, 9)

scores = [player1.score, player2.score, player3.score]

for i in scores:
  highest = scores[0]
  if i > highest:
    highest = i

print(f"highest score: {highest}")