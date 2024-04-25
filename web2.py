# web2.py 
#웹서버 페이지 실행 요청
import urllib.request
#크롤링
from bs4 import BeautifulSoup

#URL주소
url = "https://www.daangn.com/fleamarket/" 
page = urllib.request.urlopen(url).read() 
#검색이 용이한 객체 
soup = BeautifulSoup(page, "html.parser")

posts = soup.find_all("div", attrs={"div":"card-desc"})

    # <div class="card-desc">
    #   <h2 class="card-title">아이폰 13 미니  256GB</h2>
    #   <div class="card-price ">
    #     100,000원
    #   </div>
    #   <div class="card-region-name">
    #     경기도 동두천시 송내동
    #   </div>