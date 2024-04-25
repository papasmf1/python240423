# DemoStr.py 

# print(dir(str))

strA = "python is very powerful"
strB = "파이썬은 강력해"

print(len(strA))
print(len(strB))
print(strA.capitalize())
print(strA.count("p"))
print(strA.count("p", 7))
print(strA.startswith("py"))
print(strA.endswith("ful"))
print("MBC2580".isalnum())
print("MBC:2580".isalnum())
print("2580".isdecimal())

print("---반복 문자열 생성---")
names = ["박문수","이순신","김길동"]
for name in names:
    print("안녕하세요 {0}님 벌써 여름입니다!".format(name))
    print("="*40)

print("---문자열 가공---")
data = "<<<  피자 햄버거 치킨  >>>"
result = data.strip("<> ")
print(data)
print(result)
result2 = result.replace("피자", "피자 빵")
print(result2)


