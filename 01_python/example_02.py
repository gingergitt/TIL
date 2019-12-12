import requests
import webbrowser
from bs4 import BeautifulSoup
from datetime import datetime
# webbrowser.open('www.google.com')
# webbrowser.open_new('www.naver.com')
# webbrowser.open_new_tab('www.daum.net')


# res = requests.get('http://apple.kr')
# # print(res)
# # print(res.text) #주소안의 모든 텍스트가 나타난다. 
# print(res.status_code) #200번(서버가정상일때)이 나오는지 확인하기 위한 코드 (404나오는지 확인하는 ) -->상태정보만확인
# print(res.text)


url = 'https://finance.naver.com/sise/'
response = requests.get(url).text
soup = BeautifulSoup(response,'html.parser')
kospi = soup.select_one('#KOSPI_now') 
print(kospi.text)
#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child(5) > li:nth-child(4) > a > span.ah_k
#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul > li > a > span.ah_k


#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li:nth-child(12)
#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li. ah_k




#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li:nth-child(12) > a
url = 'https://naver.com/'
response = requests.get(url).text
soup = BeautifulSoup(response,'html.parser')
now = datetime.now()
search = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div > ul > li .ah_k') 
print(f'{now}기준 실시간 검색어') #변화하는 변수의 내용들을 받아서 처리할 수 있게 해주는 함수 --> f
# for name in search:
#     print(name.text)


# print(search)


for i, name in enumerate(search):
    print(f'{i+1}위: {name.text}')