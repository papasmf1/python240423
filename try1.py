# try1.py 
#함수 정의
def divide(a,b):
    return a/b 

#에러 처리 추가
try: 
    #호출
    result = divide(5, 2)
except ZeroDivisionError:
    print("0으로 나누면 안됩니다.")
except TypeError:
    print("숫자여야 연산이 됩니다.")
else:
    print("계산결과:{0}".format(result))
finally:
    print("무조건 실행(한번 더 체크)")

print("전체 코드 실행 종료")

