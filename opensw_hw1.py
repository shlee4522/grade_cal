students = [] #학생 정보 리스트

def student_info():
  for i in range(5):
    name = input(f"{i+1}번째 학생 이름: ")
    scores = [int(x) for x in input("영어, C언어, 파이썬 점수 : ").split()]
    student = {"name": name, "scores": scores}
    students.append(student)

def calculate_total_score(scores):
  return sum(scores)

def calculate_average_score(total_score):
  return total_score / 3

def calculate_grade(average_score):
  if average_score >= 90:
    return "A"
  elif average_score >= 80:
    return "B"
  elif average_score >= 70:
    return "C"
  elif average_score >= 60:
    return "D"
  else:
    return "F"

def calculate_rank(students):
  sorted_students = sorted(students, key=lambda student: student["total_score"], reverse=True)

  ranks = {}
  for i, student in enumerate(sorted_students):
    ranks[student["name"]] = i + 1

  return ranks

student_info()

for student in students:
  total_score = calculate_total_score(student["scores"])
  student["total_score"] = total_score

  average_score = calculate_average_score(total_score)
  student["average_score"] = average_score

  grade = calculate_grade(average_score)
  student["grade"] = grade

ranks = calculate_rank(students)

print("=" * 30)
print("  학생 성적 결과")
print("=" * 30)

for student in students:
  print(f"이름: {student['name']}")
  print(f"- 영어: {student['scores'][0]}")
  print(f"- C언어: {student['scores'][1]}")
  print(f"- 파이썬: {student['scores'][2]}")
  print(f"- 총점: {student['total_score']}")
  print(f"- 평균: {student['average_score']}")
  print(f"- 학점: {student['grade']}")
  print(f"- 등수: {ranks[student['name']]}")
  print()

print("=" * 30)