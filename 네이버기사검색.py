import requests
from bs4 import BeautifulSoup

def get_article_titles(url):
    # URL에서 HTML 가져오기
    response = requests.get(url)
    html = response.text
    
    # BeautifulSoup을 사용하여 HTML 파싱
    soup = BeautifulSoup(html, 'html.parser')
    
    # 기사 제목을 담을 리스트 초기화
    article_titles = []
    
    # 제목을 포함한 요소 찾기
    titles = soup.find_all('a', {'class': 'news_tit'})
    
    # 각 제목에서 텍스트 추출하여 리스트에 추가
    for title in titles:
        article_titles.append(title.get_text())
    
    return article_titles

# 크롤링할 주소
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%B0%98%EB%8F%84%EC%B2%B4"

# 기사 제목 크롤링
titles = get_article_titles(url)

# 결과 출력
for idx, title in enumerate(titles, start=1):
    print(f"{idx}. {title}")
