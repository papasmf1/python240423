class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def printInfo(self):
        #파이썬 3.6이상은 포맷 스트링 
        print(f"ID: {self.id}, Name: {self.name}")

class Manager(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)
        self.title = title
    
    def printInfo(self):
        super().printInfo()
        print(f"Title: {self.title}")

class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)
        self.skill = skill
    
    def printInfo(self):
        super().printInfo()
        print(f"Skill: {self.skill}")

# 10개의 샘플 생성
samples = [
    Manager(1, "John Doe", "Senior Manager"),
    Employee(2, "Jane Smith", "Python"),
    Manager(3, "Alice Lee", "Project Manager"),
    Employee(4, "Bob Johnson", "Java"),
    Manager(5, "Eva Martinez", "Director"),
    Employee(6, "Michael Brown", "JavaScript"),
    Manager(7, "Sarah Clark", "Team Lead"),
    Employee(8, "David Wilson", "C++"),
    Manager(9, "Emily Taylor", "VP of Engineering"),
    Employee(10, "Chris Garcia", "SQL"),
]

# 생성된 샘플 정보 출력
for sample in samples:
    sample.printInfo()
    print()  # 각각의 정보를 구분하기 위한 줄 바꿈
