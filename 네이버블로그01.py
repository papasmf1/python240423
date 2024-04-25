import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# 결과를 담을 리스트 초기화
result = []

# 1페이지부터 100페이지까지 순회
for page in range(1, 101):
    # 크롤링할 주소
    url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query=%EC%95%84%EC%9D%B4%ED%8F%B015&start={page * 10 - 9}"
    
    # HTTP 요청을 보내고 응답 받기
    response = requests.get(url)
    
    # 응답 받은 HTML을 BeautifulSoup을 이용하여 파싱
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 블로그 정보가 들어있는 태그 선택
    blog_list = soup.select('.api_txt_lines.total_tit')
    
    # 각 블로그 정보에 대해 순회
    for blog in blog_list:
        # 블로그명
        blog_name = blog.text.strip()
        # 블로그 주소
        blog_link = blog['href']
        # 글의 제목
        post_title = blog.parent.select('.total_sub')[0].text.strip()
        # 포스팅 날짜
        post_date = blog.parent.select('.sub_time.sub_txt')[0].text.strip()
        
        # 결과 리스트에 정보 추가
        result.append({
            'blog_name': blog_name,
            'blog_link': blog_link,
            'post_title': post_title,
            'post_date': post_date
        })

# 엑셀 파일 생성
wb = Workbook()
ws = wb.active

# 열 제목 추가
ws.append(['블로그명', '블로그주소', '글의제목', '포스팅날짜'])

# 결과를 엑셀 파일에 추가
for entry in result:
    ws.append([entry['blog_name'], entry['blog_link'], entry['post_title'], entry['post_date']])

# 엑셀 파일 저장
wb.save("blog_crawling_results.xlsx")
