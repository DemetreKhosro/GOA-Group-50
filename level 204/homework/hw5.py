# 5) შექმენი კლასი Subscription: რომელსაც ექნება user_name, plan("free", "basic", "pro"), months_active. წესები: free -> max 1 month, basic -> max 6 months, pro -> unlimited. დაბეჭდე რომელ მომხმარებლებს აქვთ ვალიდური subscription. ლოგიკა დაწერე class-ის გარეთ

class Subscription:
  def __init__(self, user_name, plan, months_active):
    self.user_name = user_name
    self.plan = plan
    self.months_active = months_active

subscriptions = [
  Subscription("gio", "free", 1),
  Subscription("ani", "free", 2),
  Subscription("luka", "basic", 4),
  Subscription("saba", "basic", 7),
  Subscription("toma", "pro", 12)
]

for sub in subscriptions:
  is_valid = False
  if sub.plan == "free" and sub.months_active <= 1:
    is_valid = True
  elif sub.plan == "basic" and sub.months_active <= 6:
    is_valid = True
  elif sub.plan == "pro":
    is_valid = True

  if is_valid:
    print(sub.user_name, sub.plan, sub.months_active)