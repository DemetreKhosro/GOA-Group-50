class VowelCounter:
  def __init__(self, text):
    self.text = text
    self.vowels = 'aeiou'

  def count(self):
    vowel_count = 0
    filtered_text = self.text.lower()

    for char in filtered_text:
      if char in self.vowels:
        vowel_count += 1
    return vowel_count

try:
  with open('level 205/homework/hw.txt', 'r') as f:
    content = f.read()
  
  counter = VowelCounter(content)
  print(f"vowel count: {counter.count()}")
except FileNotFoundError:
  print('file not found')