import requests
import parsel
import re
import os
import pdfkit
yu=input('请输入需要爬取的csdn网页url:')
url=f'{yu}'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
}
html = requests.get(url=url,headers=headers).text
print('网页响应成功，正在保存...')
selector = parsel.Selector(html)
title = re.findall('<title>(.*?)</title>',html)[0]
centent = selector.css('#content_views').get()
str_html = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
</head>
<body>
    {centent}
</body>
</html>'''
save_path = r'E:\桌面\爬虫数据收集\html'
if not os.path.exists(save_path):
    os.makedirs(save_path)
config = pdfkit.configuration(wkhtmltopdf=r'D:\\htmtmltopdf.exltopdf\\wkhtmltopdf\\bin\\wkhe')
with open(os.path.join(save_path, f'{title}.html'), mode='w', encoding='UTF-8') as f:
    f.write(str_html)
html_path = r'E:\桌面\爬虫数据收集\html\\'+title+'.html'
pdf_path = r'E:\桌面\爬虫数据收集\pdf\\'+title+'.pdf'
pdfkit.from_file(html_path,pdf_path,configuration=config)



print('保存成功')


