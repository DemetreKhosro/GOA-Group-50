# 1) შექმენი კლასი Student, რომელსაც ექნება:name,age,grade. __init__-ის გამოყენებით.შემდეგ: შექმენი 2 სტუდენტის ობიექტი და დაბეჭდე მათი მონაცემები

class Student:
  def __init__(self, name, age, grade):
    self.name = name
    self.age = age
    self.grade = grade

student1 = Student('Demetre', 14, 9)
student2 = Student('John', 15, 10)

print(student1)
print(student2)