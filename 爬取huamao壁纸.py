import requests
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
}
# 按f12然后动态刷新，在fetch/xhr里面寻找，后期打算升级功能，利用selenium模拟操作。
reporturl=input('请输入需要爬取页面的请求url:')
url2=f"{reporturl}"
piliang = requests.get(url=url2,headers=header).json()
result = piliang['results']
url = "https://huamaobizhi.com/normal-download/"
q = 0;
for i in result:
    q=q+1
    num = i['id']
    title = i['tit']
    data = {
        'wallpaperId': num
    }
    url1=f"https://huamaobizhi.com/details/{num}?lang=zh-CN"
    html = requests.get(url=url1,headers=header).text
    w=str(q)
    print('正在载入第'+w+'张')
    download = requests.post(url=url,headers=header,data=data).content
    pdf_path = r'E:\桌面\图片\\'+title+'.jpg'
    with open(pdf_path,mode='wb') as f:
        f.write(download)
    print('成功抓取')