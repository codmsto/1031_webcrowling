import requests
from bs4 import BeautifulSoup

#URL -> 제목, 기자 , 날짜 , 본문 수집
def get_news_info(url:str):
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    title = doc.select("he.tit_view")[0].get_text()
    contents = doc.select("section > p")  
    content = ""
    for text in contents:
        content += text.get_text()  
    writer = doc.select("span.txt_info")[0].get_text()
    reg_date = doc.select("span.num_date")[0].get_text()
    list_date = reg_date.split(".")
    list_date = list(map(lambda x: x.strip(), list_date))
    reg_date = list_date[0] + list_date[1] + list_date[2]




