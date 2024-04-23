# DemoLoop.py 

value = 5 
while value > 0:
    print(value)
    value -= 1 


lst = [100, "apple", 3.14]
for i in lst:
    print(i)

d = {"apple":5, "kiwi":10}
for k,v in d.items():
    print(k,v)


#구구단 출력
for x in [2,3,4,5,6]:
    print("---{0}단---".format(x))
    for y in [1,2,3,4,5,6,7,8,9]:
        print("{0} * {1} = {2}".format(x, y, x*y))


print("---break구문---")
lst = list(range(1,11))
print(lst)
for i in lst:
    if i > 5:
        break 
    print(i)

print("---continue구문---")
for i in lst:
    if i % 2 == 0:
        continue
    print(i)

print("---수열함수---")
print(list(range(2000,2025)))
days = list(range(1,32))
print(days) 

print("---리스트 컴프리헨션----")
lst = list(range(1,11))
print([i**2 for i in lst if i > 5])
tp = ("apple", "kiwi")
print([len(i) for i in tp])

print("---필터링---")
lst = [10, 25, 30]
iterL = filter(None, lst)
for item in iterL:
    print(item)

print("---필터링 함수 준비---")
def getBiggerThan20(i):
    return i > 20 

iterL = filter(getBiggerThan20, lst)
for item in iterL:
    print(item)

    





