# DemoFormat.py 
import sys 

for i in range(10):
    url = "https://www.multi.com/?page=" + str(i) 
    print(url)

#틸드(~)
print("welcome to", "python", sep="~", end="!", file=sys.stderr)

#파일에 저장
f = open("test.txt", "wt")
print("file write", file=f)
f.close() 

#정렬방식 지정 
print("---정렬 방식---")
for x in range(1,11):
    print(x,"*",x,"=",x*x)

print("---우측 정렬 방식---")
for x in range(1,11):
    print(x,"*",x,"=",  str(x*x).rjust(5)) 

print("---0으로 채우기---")
for x in range(1,11):
    print(x,"*",x,"=",  str(x*x).zfill(5)) 

print("---서식 지정---")
print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:c}".format(65))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))




