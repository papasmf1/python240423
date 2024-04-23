# function2.py 

#기본값을 명시 
def times(a=10,b=20):
    return a*b 

#호출
print(times())
print(times(5))
print(times(5,6))

#키워드인자 방식(매개변수명을 기술)
def connectURI(server, port):
    strURL = "http://" + server + ":" + port 
    return strURL 

#호출 
print(connectURI("multi.com", "80"))
print(connectURI(port="8080", server="multi.com"))

#가변인자: 가변적인 상황(인자)
def union(*ar):
    #지역변수
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result 

#호출
print(union("HAM", "EGG"))
print(union("HAM", "EGG", "SPAM"))

#람다함수: 1회성, 즉흥적으로 함수 정의 
g = lambda a,b:a*b 
print(g(3,4))
print(g(5,6))

print( (lambda x:x*x)(3) )

print( globals() )

#람다 함수 활용 
print("---람다 함수 활용---")
lst = [10, 25, 30]
iterL = filter(lambda x:x>20, lst)
for item in iterL:
    print(item)

print( dir() )