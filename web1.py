# web1.py 
#웹 크롤링 선언
from bs4 import BeautifulSoup

#페이지를 로딩(연속으로 메서드체인)
page = open("test.html", "rt", encoding="utf-8").read() 

#검색이 용이한 객체
soup = BeautifulSoup(page, "html.parser")
#print(soup.prettify())
#<p>를 몽땅 검색 
# print(soup.find_all("p"))
#첫번째<p>
# print(soup.find("p"))
#조건을 지정: <p class='outer-text'>
#class는 키워드, class_
# print(soup.find_all("p", class_="outer-text"))
#최근 코드 attrs => attributes 
#print( soup.find_all("p", attrs={"class":"outer-text"}) )

#id=first검색 
#print(soup.find_all(id="first"))

#태그 내부의 문자열 출력: .text, get_text()메서드 
for tag in soup.find_all("p"):
    title = tag.text.strip()
    title = title.replace("\n", "")
    print(title)

