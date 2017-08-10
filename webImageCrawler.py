#-*- coding: utf-8 -*-
import requests
import os
def download_web_image2(image_url,name,folderName):

    img_data = requests.get(image_url).content
    targetFile = os.path.join(folderName, str(name)+'.jpg')
    with open(targetFile, 'wb') as handler:
            handler.write(img_data)


import requests
from lxml.html import parse
from io import StringIO
import os, sys
from PIL import Image

def main():
# 검색할 이미지의 키워드 입력

    keyword_list = ["table no background", "living table", "living table no background", "baby table", "Centre Table "
            "home table","work table", "glass table","stainless table", "square table"]
    print(len(keyword_list))
    #keyword = input("검색할 이미지를 입력하세요 : ")
    for keyword in keyword_list:
        crawler(keyword)


def crawler(keyword):  
    url = 'https://www.google.co.kr/search?q='+str(keyword)+'&source=lnms&tbm=isch&sa=X&ved=0ahUKEwic-taB9IXVAhWDHpQKHXOjC14Q_AUIBigB&biw=1842&bih=990'

    # html 소스 가져오기
#text = requests.get(url).text
    text = requests.get(url, headers={'user-agent': ':Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}).text

    # html 문서로 파싱
    text_source = StringIO(text)
    parsed = parse(text_source)

    # root node
    doc = parsed.getroot()

    imgs = doc.findall('.//img')
    
    img_list = []   # 이미지 경로가 담길 list
    index = 0
    folderName = 'Download'
    if not os.path.exists(folderName): # 폴더명
        os.makedirs(folderName)

    for a in imgs:
        if (a.get('data-src')==None):
            continue
        index += 1
        img_list.append(a.get('data-src'))
        print(a.get('data-src'))
    
        download_web_image2(a.get('data-src'),keyword+str(index),folderName)

main()
