# DemoTupleSet.py 
tp = (10, 20, 30)
print( type(tp) )
print( tp )
print(tp.index(20))
print(tp.count(10))

#함수를 정의
def calc(a,b):
    return a+b, a*b 

#함수를 호출(중단점)
result = calc(3,4)
print(result[0], result[1])

#한방에 입력 
print("id:%s, name:%s" % ("kim","김유신"))

#튜플로 입력 
args = (5,6)
print(calc(*args))


#세트형식 
print("---세트형식---")
a = {1,2,3,3}
b = {3,4,4,5}
print(a)
print(b)
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print( a | b )
print( a & b )
print( a - b )

print("---형식 변환---")
a = set( (1,2,3) )
print(a)
b = list(a)
b.append(4)
print(b)





