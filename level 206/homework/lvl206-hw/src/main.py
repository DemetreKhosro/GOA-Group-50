current_user = None

class todolist:
  def __init__(self, task=""):
    self.task = task

  # save account
  def register(self, user, pwd):
    if len(pwd) < 8:
      print('password must be longer than 8 characters')
      return False

    with open('accounts.txt', 'a') as f:
      f.write(f"{user},{pwd}\n")
    print('registration successful')

  # save task
  def add_to_list(self, task):
    global current_user
    if not current_user:
      print('login required')
      return

    try:
      with open('tasks.txt', 'r') as f:
        for line in f:
          u, t, s = line.strip().split(',')
          if u == current_user and t == task:
            print('task already exists!')
            return
    except FileNotFoundError:
      pass

    with open('tasks.txt', 'a') as f:
      f.write(f"{current_user},{task},active\n")
    print('task added')

  # delete task
  def remove_task(self, task_name):
    global current_user
    try:
      with open('tasks.txt', 'r') as f:
        lines = f.readlines()
      with open('tasks.txt', 'w') as f:
        for line in lines:
          if not line.startswith(f"{current_user},{task_name},"):
            f.write(line)
    except FileNotFoundError:
      print('no tasks found')

  # update task
  def edit_task(self, task_name, new_status):
    global current_user
    try:
      with open('tasks.txt', 'r') as f:
        lines = f.readlines()
      with open('tasks.txt', 'w') as f:
        for line in lines:
          if line.startswith(f"{current_user},{task_name},"):
            f.write(f"{current_user},{task_name},{new_status}\n")
          else:
            f.write(line)
    except FileNotFoundError:
      print('no tasks found')

# check login
def login():
  global current_user
  u = input('user: ')
  p = input('pass: ')
  try:
    with open('accounts.txt', 'r') as f:
      for line in f:
        name, pwd = line.strip().split(',')
        if u == name and p == pwd:
          current_user = u
          print('login successful')
          return True
  except FileNotFoundError:
    print('no accounts found')
  return False

manager = todolist()

while True:
  print(f"\ncurrent user: {current_user}")
  print('1. register\n2. login\n3. add task\n4. edit task\n5. remove task\n6. exit')
  action = input('enter a number (1-6): ')
  if action == "1":
    manager.register(input('name: '), input('pass: '))
  elif action == "2":
    login()
  elif action == "3":
    manager.add_to_list(input('add task: '))
  elif action == "4":
    manager.edit_task(input('edit task: '), input('status (done/active): '))
  elif action == "5":
    manager.remove_task(input('remove task: '))
  elif action == "6":
    break