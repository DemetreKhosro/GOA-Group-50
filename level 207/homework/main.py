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

analysis = AnalyzeText('level 207/homework/text.txt')
print(f"თხრობითი წინადადებები: {analysis.count_narrative()}")
print(f"კითხვითი წინადადებები: {analysis.count_questions()}")