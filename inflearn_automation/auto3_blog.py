# https://www.inflearn.com/course/lecture?courseSlug=%EC%97%85%EB%AC%B4%EC%9E%90%EB%8F%99%ED%99%94-%ED%8C%8C%EC%9D%B4%EC%8D%AC-pyautogui-%ED%81%AC%EB%A1%A4%EB%A7%81%EA%B8%B0%EC%B4%88&unitId=27335&tab=curriculum

from bs4 import BeautifulSoup
import requests

base_url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="
keyword = input("enter search keyword : ")

search_url = base_url + keyword
#print(search_url)

r = requests.get(search_url)

soup = BeautifulSoup(r.text, "html.parser")

items = soup.select(".title_area")

for index, item in enumerate(items, 1):    
    print(f"{index} ", item.text)
    