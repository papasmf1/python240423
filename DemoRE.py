# DemoRE.py 
#정규표현식
import re 

#검색한 결과를 매칭오브젝트로 리턴 
result = re.search("[0-9]*th", "  35th")
print(result)
print(result.group())

# result = re.match("[0-9]*th", "  35th")
# print(result)
# print(result.group())

print("---연도---")
result = re.search("\d{4}", "올해는 2024년입니다.")
print(result.group())

print("---우편번호---")
result = re.search("\d{5}", "우리동네는 51333")
print(result.group())

print("---단어 검색---")
result = re.search( "apple", "this is Apple".lower() )
print(result.group())

print("---시작 패턴---")
result = re.search( "^this", "this is Apple".lower() )
print(result.group())
