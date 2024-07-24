import requests
import time
import hashlib
import re
# def get_data():
#     # s = ['NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt',
#     #      'appid=1014',
#     #      f'clienttime={time.time()}',
#     #      'clientver=20000',
#     #      "dfid=2mRyxw4RLOqY1EsGk31nnwx5",
#     #      "encode_album_audio_id=j2sek95",
#     #      "mid=e4831702920bb9b873b094956affda0e",
#     #      "platid=4",
#     #      "srcappid=2919",
#     #
#     #      'NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt']
# #     s = [
# #       "NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt",
# #       "appid=1014",
# #       f"clienttime={int(time.time())}",
# #       "clientver=20000",
# #       "dfid=2C6tLO2W7sBu3Wn1WB0cbSzf",
# #       "encode_album_audio_id=nkket74",
# #       "mid=aabef9bd17da0695c400f6c992a78b71",
# #       "platid=4",
# #       "srcappid=2919",
# #       "token=",
# #       "userid=0",
# #       "uuid=aabef9bd17da0695c400f6c992a78b71",
# #       "NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt"
# # ]
#     s = [
#         "NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt",
#         "appid=1014",
#         f"clienttime={int(time.time())}",  # 时间戳
#         "clientver=20000",
#         "dfid=11S5Hd0E3dhq3jHxZ90dzFYU",
#         f"encode_album_audio_id=j410q60",  # 歌曲ID
#         "mid=8b5710fdab09aea0e4649de3e430ad23",
#         "platid=4",
#         "srcappid=2919",
#         "token=",
#         "userid=0",
#         "uuid=8b5710fdab09aea0e4649de3e430ad23",
#         "NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt"
#     ]
#     string = ''.join(s)
#     MD5 = hashlib.md5()
#     MD5.update(string.encode('utf-8'))
#     signature = MD5.hexdigest()
#     print(signature)
#     return signature
# get_data()
headers= {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0',
    'Referer':'https://www.kugou.com/',
}
# url = 'https://wwwapi.kugou.com/play/songinfo'
#
# data = {
#     'srcappid':'2919',
#     'clientver':'20000',
#     'clienttime':'1704522723326',
#     'mid':'aabef9bd17da0695c400f6c992a78b71',
#     'uuid':'aabef9bd17da0695c400f6c992a78b71',
#     'dfid':'2C6tLO2W7sBu3Wn1WB0cbSzf',
#     'appid':'1014',
#     'platid':'4',
#     'encode_album_audio_id':'j410q60',
#     'token':'',
#     'userid':'0',
#     'signature':f'{get_data()}'
# }

petten = r'<audio id="myAudio" class="music" src="(.*?)" preload="auto" >'

url = "https://www.kugou.com/mixsong/j410q60.html?fromsearch=%E6%99%B4%E5%A4%A9"
# //*[@id="myAudio"]
html = requests.get(url,headers=headers).text
match = re.findall(petten,html)
for i in  match:
    print(i)
# audio_name = html['data']['audio_name']
# play_url = html['data']['play_url']
# music = requests.get(url=play_url,headers=headers).content
# with open(f"{audio_name}.mp3",mode='wb') as f:
#     f.write(music)
# print(html)