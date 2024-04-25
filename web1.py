# web1.py 
#웹 크롤링 선언
from bs4 import BeautifulSoup

#페이지를 로딩(연속으로 메서드체인)
page = open("test.html", "rt", encoding="utf-8").read() 

#검색이 용이한 객체
soup = BeautifulSoup(page, "html.parser")
print(soup.prettify())

