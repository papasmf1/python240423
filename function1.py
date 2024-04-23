# function1.py 

#1)함수 정의
def setValue(newValue):
    #지역변수
    x = newValue
    print("지역변수:", x)

#2)함수 호출
retValue = setValue(5)
print(retValue)

#함수 정의
def swap(x,y):
    return y,x 

#호출
retValue = swap(3,4)
print(retValue)

print("---불변형식---")
a = 1.2 
print(id(a))
a = 2.3 
print(id(a))

print("---가변형식---")
lst = [1,2,3]
print(id(lst))
lst.append(4)
print(id(lst))

print("---지역변수---")
#함수 정의 
def func(a):
    #지역변수 초기화 
    x = 5 
    return a+x 

#호출 
print(func(1))

print("---전역변수---")
x = 10 
def func2(a):
    return a+x 

#호출
print(func2(1))