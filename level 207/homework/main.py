class AnalyzeText:
  def __init__(self, filename):
    self.filename = filename

    try:
      with open(self.filename, 'r', encoding='utf-8') as f:
        self.content = f.read()
    except FileNotFoundError:
      self.content = ''
      print('file not found')

  def count_narrative(self):
    return self.content.count('.')
  
  def count_questions(self):
    return self.content.count('?')
  

analysis = AnalyzeText('level 207/homework/text.txt')
print(f"თხრობითი წინადადებები: {analysis.count_narrative()}")
print(f"კითხვითი წინადადებები: {analysis.count_questions()}")