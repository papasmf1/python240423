import re

def check_email(email):
    # 이메일 주소 패턴
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    '''
    - ^: 문자열의 시작을 나타냅니다.
    - [\w\.-]+: 사용자 이름 부분을 나타냅니다. 
                \w는 단어 문자(알파벳, 숫자, 언더스코어)를 의미하고,
                \.은 마침표를 의미합니다. -은 하이픈을 의미합니다.
                따라서 [\w\.-]+는 사용자 이름 부분이 알파벳, 숫자, 언더스코어, 마침표, 하이픈으로 이루어져 있고 최소 한 글자 이상인 것을 의미합니다.
    - @: 이메일 주소의 사용자 이름과 도메인 부분을 구분하는 기호입니다.
    - [\w\.-]+: 도메인 부분을 나타냅니다. 사용자 이름 부분과 동일한 패턴을 가지고 있습니다.
    - \.: 도메인의 최상위 도메인(TLD) 앞에 있는 마침표를 나타냅니다.
    - \w+: TLD를 나타냅니다. 알파벳과 숫자로 이루어진 최소 한 글자 이상의 문자열입니다.
    - $: 문자열의 끝을 나타냅니다.
    '''
    
    # 이메일 주소 검사
    if re.search(pattern, email):
        return True
    else:
        return False

# 샘플 데이터
sample_emails = [
    "user@example.com",
    "user.name@example.com",
    "user123@example.com",
    "user-name@example.com",
    "user@example.co.kr",
    "user@sub.example.com",
    "user123@sub.example.co.kr",
    "user.name123@example.com",
    "user@example.com.au",
    "user123@example"
]

# 이메일 주소 체크
for email in sample_emails:
    print(f"{email}: {'유효' if check_email(email) else '유효하지 않음'}")
