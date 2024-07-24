import requests
import csv
f = open('data.csv',mode='w',newline='')
csv_writer = csv.DictWriter(f,fieldnames=[
    '标题',
    '价格',
    '销量',
    '详情链接',
    '商品图片',
    '店铺名',
    '公司名'
])
csv_writer.writeheader()
x=int(input("从第几页开始:"))
y=int(input("到第几页结束:"))
y+=1
for ww in range(x,y):
    for mun in range(1,7):
        url = f"https://p4psearch.1688.com/hamlet/async/v1.json?beginpage={ww}&asyncreq={mun}&keywords=&keyword=%E6%83%85%E8%B6%A3%E5%86%85%E8%A1%A3%E6%80%A7%E6%84%9F&sortType=&descendOrder=&province=&city=&priceStart=&priceEnd=&dis=&ptid=hreeda04653ba65c&exp=pcSemWwClick%3AB%3BofferWwClick%3AA%3Bqztf%3AE%3Blantu%3AC&cosite=bingjj_pz&salt=17211918348386&sign=7f27b037c3ccdcdbaf7c426ad7c21a16&hmaTid=3&hmaQuery=graphDataQuery&pidClass=pc_list_336&cpx=cpc%2Cfree%2Cnature&api=pcSearch"
        headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
        }
        html = requests.get(url=url,headers=headers).json()
        listdata = html['module']['offer']['list']
        for i in listdata:
            dit = {
                '标题':i['subject'],
                '价格':i['price'],
                '销量':i['saleVolume'],
                '详情链接':i['odUrl'],
                '商品图片':i['imgUrl'],
                '店铺名': i['loginId'],
                '公司名': i['company']
            }
            csv_writer.writerow(dit)
        print('正在爬取第'+str(ww)+'页的第'+str(mun*20)+'条数据')
