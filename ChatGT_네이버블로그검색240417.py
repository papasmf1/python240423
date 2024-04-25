import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

search_keyword='맥북에어'

url = f'https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}'

response = requests.get(url)


soup = BeautifulSoup(response.text, 'html.parser')

# create a new Excel workbook and select the active sheet\
wb = Workbook()
ws = wb.active

# write the column names to the first row of the sheet
ws.append(["블로그명", "블로그주소", "글 제목", "포스팅 날짜"])

for page in range(1, 100):
    url = f'https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}&start={page * 10 - 9}'

    
    posts = soup.find_all('div', {'class':'fds-collection-root jbpl1VtDuaF1y0OLVw6I'})
    for post in posts:
        try:
            #<a nocr="1" href="https://in96%B4" class="kbBffxjPwyVTeP10JD3y fds-info-inner-text" target="_blank"><span class="WlLgJQM1F90CPjOFn4AM">그남자 원동욱</span></a>
            #<span class="WlLgJQM1F90CPjOFn4AM">그남자 원동욱</span>
            blog_address_elem = post.find("a", 
                attrs={"class":"kbBffxjPwyVTeP10JD3y fds-info-inner-text"}) 
            blog_address = blog_address_elem["href"]
            blog_address_title_elem = post.find("span", attrs={"class":"WlLgJQM1F90CPjOFn4AM"})
            blog_address_title = blog_address_title_elem.text 
        except TypeError:
            blog_address = "" 
            blog_address_title = ""
        
        #<span class="WlLgJQM1F90CPjOFn4AM"><mark>맥북에어</mark>M3 13인치,<mark>맥북</mark>프로M3 14인치 가격 스펙 비교</span>
        #<span class="fds-info-sub-inner-text WlLgJQM1F90CPjOFn4AM">2주 전</span>
        #<a nocr="1" href="https://blo" class="fwA5zB9fKvQZcIwEGZoQ fds-comps-right-image-text-title" target="_blank" data-cb-target="'SYS-0000000035493126.90000003_000000000000003403434C3B'" data-cb-trigger="true"><span class="m4k_AnOFgU2P631SabRj"><mark>아이폰15</mark> 색상 순위 고민 구입 꿀팁!</span></a>
        #<a nocr="1" href="https://in.nav4" class="kbBffxjPwyVTeP10JD3y fds-comps-right-image-text-content" target="_blank" data-cb-target="'SPC-0000000000009106.a0209rl4_nblog_post_223413866837'" data-cb-trigger="true"><span class="WlLgJQM1F90CPjOFn4AM">자, 여기까지 <mark>맥북 에어</mark> M3 13 인치 부터 <mark>맥북</mark>프로 M3 14 인치 스펙과 비교를 해보았습니다. <mark>에어</mark>는 옆그레이드, 프로는 업그레이드가 된 만큼 비교를 해보시기 바라며 저는 이만 마치도록 하겠습니다. <mark>맥북</mark> M3 시리즈 사전예약하기 #<mark>맥북에어</mark> #<mark>맥북에어</mark>M3 #<mark>맥북에어</mark>M3 #<mark>맥북에어</mark></span></a>
        
        post_date_elem = post.find('span', {'class':'fds-info-sub-inner-text WlLgJQM1F90CPjOFn4AM'})
        post_date = post_date_elem.text if post_date_elem else ""
        post_title_elem = post.find("a", attrs={"class":"kbBffxjPwyVTeP10JD3y fds-comps-right-image-text-content"})
        post_title = post_title_elem.text if post_title_elem else "" 

        print(blog_address)
        print(blog_address_title)
        print(post_title)
        print(post_date)

        ws.append([blog_address_title, blog_address, post_title, post_date])

#path = 'c:\\work\\'
#file_path = f'{path}{search_keyword}_blog_data.xlsx'
file_path = f'{search_keyword}_blog_data.xlsx'
wb.save(file_path)