# Chap05_self누락_이름충돌.py
strName = "Not Class Member"
class DemoString:
    def __init__(self):
        self.strName = "" 
    def set(self, msg):
        self.strName = msg
    def print(self):
        print(strName)

g = DemoString()
g.set("First Message")
g.print()
