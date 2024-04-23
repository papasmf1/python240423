# Chap05_생성자와소멸자.py 

class MyClass:
    def __init__(self, value):
        self.value = value
        print("Instance is created! Value = ", value)
    def __del__(self):
        print("Instance is deleted!")

#인스턴스 생성 
d = MyClass(10)
#참조카운트를 1에서 0으로 만들면 소멸
del d

print("전체 코드 실행 종료")




