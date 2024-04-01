# https://www.inflearn.com/course/lecture?courseSlug=%EC%97%85%EB%AC%B4%EC%9E%90%EB%8F%99%ED%99%94-%ED%8C%8C%EC%9D%B4%EC%8D%AC-pyautogui-%ED%81%AC%EB%A1%A4%EB%A7%81%EA%B8%B0%EC%B4%88&unitId=27336&tab=curriculum

from bs4 import BeautifulSoup
import requests

base_url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="
#keyword = input("enter search keyword : ")
keyword = "대전 청년 월세 신청"

search_url = base_url + keyword
#print(search_url)

r = requests.get(search_url)

soup = BeautifulSoup(r.text, "html.parser")

items = soup.find_all(class_="view_wrap")

for index, item in enumerate(items, 1):      
    blog_title = item.find(class_="user_box_inner").text
    post_title = item.find(class_="title_link").text
    link = item.find(class_="title_link").attrs['href']
    ##main_pack > section > div.api_subject_bx > ul > li:nth-child(1) > div > div.user_box > div.user_box_inner > div
    print(f"<<{index}>>")
    print(blog_title)
    print(post_title)
    print(link)
    link1 = item.find(class_="title_link")
    print(link1['href'])
    print(link1.get('href'))
    print()
    
    if link == "https://blog.naver.com/nuri00kor/223368980255":
        r = requests.get(link)
        print("visit navy!")
        break
    
    ###########################

import pyautogui
pyautogui.moveTo(547,952)
pyautogui.keyDown('ctrl') # ctrl 키를 누른 상태를 유지합니다.
pyautogui.click()
pyautogui.keyUp('ctrl') # ctrl 키를 뗍니다.

import time
time.sleep(3)
pyautogui.press('enter')



    