class AnalyzeText:
  def __init__(self, filename):
    self.filename = filename

    try:
      with open(self.filename, 'r', encoding='utf-8') as f:
        self.content = f.read()
    except FileNotFoundError:
      self.content = ''
      print('file not found')

  # თხრობითი წინადადებების დათვლა
  def count_narrative(self):
    count = 0
    # ვალიდაცია სამი წერტილისთვის
    for i in range(len(self.content)):
      if self.content[i] == '.':
        if i == 0:
          count += 1
        elif self.content[i-1] == '.':
          continue
        else:
          count += 1
    return count
  
  # კითხვითი წინადადებების დათვლა
  def count_questions(self):
    return self.content.count('?')
  
  def write_text(self, new_text):
    try:
      with open(self.filename, 'w', encoding='utf-8') as f:
        f.write(new_text)
    except FileNotFoundError:
      print('file not found')

  def find_palinromes(self):
    palindromes = []
    words = self.content.split()

    for word in words:
      word = word.strip().strip('.?').lower()
      if len(word) <= 2:
        continue
      elif word == word[::-1]:
        palindromes.append(word)
    return palindromes


print()

analysis = AnalyzeText('level 207/homework/text.txt')
analysis.write_text('This is a new sentence... Is this a question? racecar. rogor?\n')
print(f"თხრობითი წინადადებები: {analysis.count_narrative()}")
print(f"კითხვითი წინადადებები: {analysis.count_questions()}")
print(f"პალინდრომები: {analysis.find_palinromes()}")

print()