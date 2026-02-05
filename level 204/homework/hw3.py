# 3) შექმენი კლასი ExamResult: რომელსაც ექნება student_name, math, english, science. შექმენი 2 სტუდენტი და დაბეჭდე: ვის აქვს ჯამური ქულა მეტი

class ExamResult:
  def __init__(self, student_name, math, english, science):
    self.student_name = student_name
    self.math = math
    self.english = english
    self.science = science

student1 = ExamResult('John', 83, 91, 75)
student2 = ExamResult('Nick', 74, 95, 79)

student1_sum = student1.math + student1.english + student1.science
student2_sum = student2.math + student2.english + student2.science

if student1_sum > student2_sum:
  print(f"{student1.student_name}s score is higher than {student2.student_name} score")
elif student1_sum == student2_sum:
  print('both students scores are equal')
else:
  print(f"{student2.student_name}s score is higher than {student1.student_name} score")