"""
공실박스 - 상가 긁어오기
"""

from bs4 import BeautifulSoup
import requests

base_url = "https://gongsilbox.com/maps/Xsg?lat=36.3487005&lng=127.2962388&zoom=18&r=w:9a722b5f-fcdc-40bd-a067-14c4ffdfa439"
keyword = ""
search_url = base_url + keyword

r = requests.get(search_url)
#print(search_url)
soup = BeautifulSoup(r.text, "html.parser")

# 전체 결과 출력
print(soup.prettify())



# items = soup.find_all('div', class_='w-full flex flex-wrap gap-1')
# #print(items)
# #items = soup.select(".w-full.flex.justify-start.gap-1")
# print(f"len : {len(items)}")
# for index, item in enumerate(items,1):
#     print(f"<<{index}>> {item}")
#     print()
    



# for index, item in enumerate(items, 1):      
#     blog_title = item.find(class_="user_box_inner").text
#     post_title = item.find(class_="title_link").text
#     link = item.find(class_="title_link").attrs['href']
#     ##main_pack > section > div.api_subject_bx > ul > li:nth-child(1) > div > div.user_box > div.user_box_inner > div
#     print(f"<<{index}>>")
#     print(blog_title)
#     print(post_title)
#     print(link)
#     link1 = item.find(class_="title_link")
#     print(link1['href'])
#     print(link1.get('href'))
#     print()
    
#     if link == "https://blog.naver.com/nuri00kor/223368980255":
#         r = requests.get(link)
#         print("visit navy!")
#         break
    
#     ###########################

# import pyautogui
# pyautogui.moveTo(547,952)
# pyautogui.keyDown('ctrl') # ctrl 키를 누른 상태를 유지합니다.
# pyautogui.click()
# pyautogui.keyUp('ctrl') # ctrl 키를 뗍니다.

# import time
# time.sleep(3)
# pyautogui.press('enter')



    