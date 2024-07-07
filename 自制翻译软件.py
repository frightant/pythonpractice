import time
import requests
import execjs
import ttkbootstrap as ttk
import pyttsx3

def sign(word):
    with open('temp.js',encoding='utf-8') as f:
        text=f.read()
    jscode = execjs.compile(text)
    result = jscode.call('baidu',word)
    return result
def search(word):
    result = sign(word)
    data={
        'from':'zh',
        'to':'en',
        'query':word,
        'transtype':'translang',
        'simple_means_flag':'3',
        'sign':result,
        'token':'1bf0ec42272ee53aa3334a63fe665037',
        'domain':'common',
        'ts':f'{time.time()}'
    }
    url = "https://fanyi.baidu.com/v2transapi?from=zh&to=en"
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
        'Cookie':'BAIDUID=2E018F48EBEE468BF0063D7AEAB47EA8:FG=1; BAIDUID_BFESS=2E018F48EBEE468BF0063D7AEAB47EA8:FG=1; BIDUPSID=2E018F48EBEE468BF0063D7AEAB47EA8; PSTM=1712551351; ZFY=aT3Hit2nhSqhrSmrv9yQ2c29ndL1vIaDx23wAHiWUDE:C; H_PS_PSSID=40304_40378_40416_40445_40511_60041_60026_60031_40080_60126; __bid_n=18ef6d3065f92964f38b97; BDUSS=lBNlRtQjdOcVR2dWN2Z1huWXV-ZEJQWFpPQ0U2OGtKQlRHa3dBVFRmTGpub0ptSVFBQUFBJCQAAAAAAAAAAAEAAABRwYKt0-DJ8bTyvNwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOMRW2bjEVtmOG; BDUSS_BFESS=lBNlRtQjdOcVR2dWN2Z1huWXV-ZEJQWFpPQ0U2OGtKQlRHa3dBVFRmTGpub0ptSVFBQUFBJCQAAAAAAAAAAAEAAABRwYKt0-DJ8bTyvNwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOMRW2bjEVtmOG; smallFlowVersion=old; RT="z=1&dm=baidu.com&si=c2ade42c-f3e0-4c71-aea9-4320f0fd6f66&ss=lybctoxm&sl=1&tt=2qb&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=3id&ul=9p2&hd=a3u"; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1720344728; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1720358084; ab_sr=1.0.1_MWI2ZTUxY2E4MTBlODNjZjU0YmVhMDcwNzQ5MTQyZDRmYzJjMTdjMzZiNTUxN2JkNTljMjE5YzZmMmM1YmE2M2Y2Njk5YTJlMTgwNjg5MzIwZjkyMjJjYmNlZWQ5YTk0Njc4MzdlOTFjOTU2OGMxZjY2MGQzMzI0Y2MxZjU2ZTUyZTIxMWI2ZDNkNjk4ZWE0OTFkNTQ3NzMxOWEyNWQwZTk0YjRiNjUyYzUxYTc1MzEwNTQ3ODFkYTAyZGQzZjVh',
        'Host':'fanyi.baidu.com',
        'Referer':'https://fanyi.baidu.com/'
    }
    html = requests.post(url=url,headers=headers,data=data).json()
    trans_result = html['trans_result']['data'][0]['dst']
    # print('翻译的结果是:'+trans_result)
    return trans_result


def show():
    engine = pyttsx3.init()
    word = input_va.get()
    translate = search(word)
    text.delete('0.0','end')
    text.insert('insert',translate)
    engine.say(word+translate)
    engine.runAndWait()

root=ttk.Window(
    title="小鱼翻译",
    themename="litera",
    size=(800,400),
)
root.place_window_center()
root.resizable(False,False)
frame = ttk.Frame()
frame.pack(pady=10)
input_va = ttk.StringVar()
ttk.Label(frame,text='请输入要翻译的内容:',font=('微软雅黑',12)).pack(side=ttk.LEFT)
ttk.Entry(frame,textvariable=input_va).pack(side=ttk.LEFT,padx=5)
ttk.Button(frame,text='搜索',command=show).pack(side=ttk.LEFT)
text_frame = ttk.Frame()
text_frame.pack()
text = ttk.Text(text_frame)
text.pack()
root.mainloop()