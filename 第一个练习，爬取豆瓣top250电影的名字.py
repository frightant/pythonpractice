
import requests
from bs4 import BeautifulSoup
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"
}
for i in range(0, 251, 25):
    q=str(i)
    url = 'https://movie.douban.com/top250?start='+q+'&filter='
    # url = f'https://movie.douban.com/top250?start={i}&filter=' 另一种写法
    htmlstr = requests.get(url,headers=headers).text
    html=htmlstr
    soup = BeautifulSoup(html,"html.parser")
    all_list = soup.findAll("span",attrs={"class":"title"})
    for list in all_list:
        list_str=list.string
        if "/" not in list_str:
            print(list_str)