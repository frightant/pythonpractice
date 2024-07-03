import requests
import re
url = "https://cn.bing.com/images/search?q=%e7%be%8e%e5%a5%b3&qpvt=%e7%be%8e%e5%a5%b3&form=IGRE&first=1"
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'

}
html = requests.get(url=url,headers=headers).text
# biaoda = r'<a class="inflnk" aria-label="(.*?)" href="(.*?)"></a>'
biaoda = r'detailV2&amp;ccid=(.*?)&amp;itb=0&amp;qpvt=%e7%be%8e%e5%a5%b3'
match = re.findall(biaoda,html)
# for i in match:
#     url1 = "https://cn.bing.com/images/search?view=detailV2&amp;ccid="+i+""
    # print(i)
print(html)
print(match)



# for i in range(len(match)):
#     # cut = re.search(shaixuan, match[i])
#     print(match[i])