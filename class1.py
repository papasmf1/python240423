# class1.py 
#1)클래스 정의 
class Person:
    #초기화 메서드
    def __init__(self):
        #인스턴스 멤버 변수
        self.name = "default name"
    def print(self):
        print("My name is {0}".format(self.name))

#2)인스턴스 생성
p1 = Person()
p2 = Person()
p1.name = "전우치"

#3)메서드 호출
p1.print() 
p2.print() 

#런타임시에 멤버변수 추가
Person.title = "new title"
print(p1.title)
print(p2.title)
print(Person.title)

#인스턴스 추가
p1.age = 30 
print(p1.age)
#선택한 블럭 주석 처리: ctrl + / 
# print(p2.age)

