import requests
import re
import os
folder_name = "网易云vip音乐"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
url="https://music.163.com/discover/toplist?id=3778678"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0"
}
petten = r'<a href="/song\?id=([\d]+)">(.+?)</a>'
html = requests.get(url,headers=headers).text
match = re.findall(petten,html)
for musicid,name in match:

    musicurl = f"https://music.163.com/song/media/outer/url?id={musicid}.mp3"
    save = requests.get(musicurl,headers=headers).content
    str_name=str(name)
    file_path = os.path.join(folder_name, str_name + '.mp3')
    if ":" in file_path:
        file_path = file_path.replace(':', '')
    with open(file_path, mode='wb') as f:
        f.write(save)
    print(name+" 下载成功！！")
    
print('网易云热歌榜单top200全部下载完成！！！')