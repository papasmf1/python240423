class Person:
  def __init__(self, id, name):
    self.id = id
    self.name = name

  def printInfo(self):
    print(f"ID: {self.id}, 이름: {self.name}")

class Manager(Person):
  def __init__(self, id, name, title):
    super().__init__(id, name)
    self.title = title

class Employee(Person):
  def __init__(self, id, name, skill):
    super().__init__(id, name)
    self.skill = skill

# 샘플 데이터 생성
people = []

# Person 클래스 샘플
people.append(Person(101, "철수"))
people.append(Person(102, "영희"))
people.append(Person(103, "민수"))

# Manager 클래스 샘플
people.append(Manager(201, "지영", "사장"))
people.append(Manager(202, "민호", "팀장"))

# Employee 클래스 샘플
people.append(Employee(301, "수진", "개발"))
people.append(Employee(302, "영주", "디자인"))
people.append(Employee(303, "현아", "마케팅"))

# 모든 사람 정보 출력
for person in people:
  person.printInfo()
  if isinstance(person, Manager):
    print(f"직책: {person.title}")
  elif isinstance(person, Employee):
    print(f"기술: {person.skill}")
  print()