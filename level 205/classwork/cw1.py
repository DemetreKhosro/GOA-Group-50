# გვაქვს ცარიელი ტექსტური ფაილი, შევქმნათ კლასი TodoList, გვქონდეს რაღაც მეთოდები რომლითაც todolistში ჩავამატებთ task-ებს, ასევე ამოვშლით თასქებს და მოვნიშნავთ შესრულებულად, ეს ყველა ასევე უნდა ჩაემატოს და წაიშალოს ცარიელი ფაილიდანაც, მაგისთვის გამოვიყენოთ file handling

class ToDoList:
  def __init__(self, task):
    self.task = task

  def add_to_list(self, task):
    with open('level 205/classwork/text.txt', 'a') as f:
      f.write(f"{self.task}\n")

  def remove_task(self, task):
    with open('level 205/classwork/text.txt', 'r') as file:
      text = file.read().strip().split('\n')
      arr = []
      for i in text:
        if i != task:
          arr.append(i)

      with open('level 205/classwork/text.txt', 'w') as f:
        f.write("\n".join(arr))


task1 = ToDoList('homework')

task1.remove_task('homework')