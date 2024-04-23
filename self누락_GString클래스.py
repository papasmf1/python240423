# Chap05_self누락_이름충돌.py
#전역변수 
strName = "Not Class Member"

class DemoString:
    #초기화 메서드 
    def __init__(self):
        #인스턴스 멤버 변수 초기화 
        self.strName = "" 
    #인스턴스 메서드 
    def set(self, msg):
        self.strName = msg
    def print(self):
        #모호한 것보다는 명시적인 것이 좋다(속담)
        print(self.strName)

g = DemoString()
g.set("First Message")
g.print()
