# -*- coding: utf-8 -*-
import requests
import re
import json
import os
from moviepy.editor import VideoFileClip, AudioFileClip

headers={
    'Cookie':"_uuid=47A9AF1D-29E5-49710-731C-1A677BA5544698089infoc; buvid_fp=1e8f6e2391d6837c4df5fb070ac8eee3; buvid3=15DBDAFF-7C79-6AEE-EEA2-3CAA61BA2B6098488infoc; b_nut=1707299899; buvid4=4B18D29A-7D92-7A00-9485-47E70B8E683D98488-024020709-zyD0tGvcZPCIL1qv8zusPA%3D%3D; DedeUserID=152047062; DedeUserID__ckMd5=01db927384a6bfa2; rpdid=|(u~)|R|km)0Ju~|~J|||ul; PVID=1; CURRENT_QUALITY=112; enable_web_push=DISABLE; header_theme_version=CLOSE; home_feed_column=5; browser_resolution=1488-742; b_lsid=352D9436_19035F73C46; bsource=search_bing; bmg_af_switch=1; bmg_src_def_domain=i0.hdslb.com; SESSDATA=dad275b4%2C1734444328%2C11f24%2A62CjDH5MGBPv9vQ3_bhXJXpbMNmW61rsN5JZz-ls8y9sLjlEYmJddTH1xumSkzPmoofNMSVkFCY1JTdkJ4SFVuNnozYmYzZjc0MGpJbXBEMXZoVWNCVjA1NnJXZ1VRZmdCTUFEakktdzNGVHlSeUVEQ3pRV1A4MGIxRTNCdnY1WUVUanFYZ3VzMVFnIIEC; bili_jct=7c779dd92bcdaacc64ac63feae8c1e77; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTkxNTE1MjgsImlhdCI6MTcxODg5MjI2OCwicGx0IjotMX0.hP6YTVVczSzClA8SbkYzob8zhrgek4bpWENPVYPslIw; bili_ticket_expires=1719151468; sid=64t3psr3; CURRENT_FNVAL=4048",
    'Referer':'https://www.bilibili.com/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
}
print("小鱼脚本测试版")
print(" ")
url= input("请粘贴要下载的b站视频的网页链接:")

print(" ")
print("正在启动小鱼脚本")
html = requests.get(url=url,headers=headers).text
print('成功读取网页....')
title = re.findall('<h1 data-title="(.*?)" title=',html)[0]
biaoDa = re.findall('__playinfo__=(.*?)</script>',html)[0]
json_data=json.loads(biaoDa)
video_url=json_data['data']['dash']['video'][0]['baseUrl']
audio_url=json_data['data']['dash']['audio'][0]['baseUrl']
print("正在进入下载中...")
video=requests.get(url=video_url,headers=headers).content
audio=requests.get(url=audio_url,headers=headers).content
print("已成功读取到视频，正在进入下载，请耐心等待，如果发生错误会有报错提示。")
with open(f'{title}.mp4',mode='wb') as f:
    f.write(video)
print("成功45%")
with open(f'{title}.mp3',mode='wb') as f:
    f.write(audio)
print("成功75%")
video = VideoFileClip(f"{title}.mp4")
audio = AudioFileClip(f"{title}.mp3")
final_clip = video.set_audio(audio)
final_clip.write_videofile(f"{title}"+"_.mp4", codec='libx264')

os.remove(f'{title}.mp4')
os.remove(f'{title}.mp3')

print("运行完成!!!")
