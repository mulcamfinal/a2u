import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import requests
from bs4 import BeautifulSoup
#import emoji
import json


# def remove_emoji(text):
#     return emoji.get_emoji_regexp().sub(u'', text)


chromedriver = "./chromedriver"
options = webdriver.ChromeOptions()
# options.add_argument("headless")
driver = webdriver.Chrome(chromedriver, options=options)

# 구글번역
driver.get("https://translate.google.com/?hl=ko&sl=ja&tl=ko&op=translate")


soup = BeautifulSoup()

url = 'https://www.instagram.com/explore/tags/%EA%B0%84%EC%8B%9D/'
headers = {"user-agent": "Mozilla/5.0"}
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')


# 이미지 다운로드
resp = requests.get(image_url, stream=True)
resp.raw.decode_content = True
shutil.copyfileobj(resp.raw, local_file)

# blog_contents_list = []
# blog_number = 1
# try:
#     while True:
#         test = driver.find_element_by_class_name("er8xn")
#         with open(f"../data/jpblog/{blog_number}.txt", "r",encoding="utf8") as file:
#             text = file.read()
#             # print(remove_emoji(text))
#             try:
#                 test.send_keys(remove_emoji(text))
#             except:
#                 None
#         # time.sleep(5)

#         time.sleep(5)
#         my_text = driver.find_elements_by_css_selector(".J0lOec")[0]
#         translated_text = my_text.text
#         blog_contents_list.append(translated_text)
#         print(len(blog_contents_list))
#         test.clear()

#         blog_number += 1
#         if blog_number == 275:
#             break

#     with open("../data/jpblog3.json", "w", encoding="utf8") as json_file:
#         st_json = json.dump(blog_contents_list, json_file, ensure_ascii=False)

# except:
#     with open("../data/jpblog3.json", "w", encoding="utf8") as json_file:
#         st_json = json.dump(blog_contents_list, json_file, ensure_ascii=False)
