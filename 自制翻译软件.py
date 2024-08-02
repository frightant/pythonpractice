import time
import requests
import execjs
import ttkbootstrap as ttk
import pyttsx3
import tkinter as tk

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


def searchjp(word):
    result = sign(word)
    data={
        'from':'zh',
        'to':'jp',
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

def show1():
    word = input_va.get()
    translate = searchjp(word)
    text.delete('0.0','end')
    text.insert('insert',translate)



def show():
    word = input_va.get()
    translate = search(word)
    text.delete('0.0','end')
    text.insert('insert',translate)




root=ttk.Window(
    title="小鱼翻译",
    themename="litera",
    size=(800,400),
)
def read():
    word = input_va.get()
    translate = search(word)
    engine = pyttsx3.init()
    if(is_english(translate)==False):
        engine.say(word)
    else:
        engine.say(translate)
    engine.runAndWait()
def is_english(s):
    for char in s:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            return True
    return False
def show_feedback_window():
    feedback_window = tk.Toplevel(root)
    feedback_window.title("我要报错")
    feedback_window.geometry("500x400")  # 可以设置一个初始大小

    # 创建一个文本框供用户输入反馈内容
    feedback_label = tk.Label(feedback_window, text="请输入反馈的问题")
    feedback_label.pack()
    feedback_text = tk.Text(feedback_window, height=10)
    feedback_text.pack(pady=20,padx=10)
    tk.Button(feedback_window,text="提交",command=feedback_window.destroy).pack()
    # 创建一个提交按钮，点击后关闭反馈窗口
    # submit_button = tk.Button(feedback_window, text="提交",command=lambda: handle_submit(feedback_text.get(1.0, 'end'), feedback_window))
    # submit_button.pack(pady=10)

# def handle_submit(feedback_content, feedback_window):
#     # 这里可以添加代码处理反馈内容，例如发送到服务器
#     # 假设反馈已经成功提交
#     success_window = tk.Toplevel(root)
#     success_window.title("提交成功")
#     success_window.geometry("200x100")
#
#     success_label = tk.Label(success_window, text="反馈已成功提交！")
#     success_label.pack(pady=20)
#
#     # 可以添加一个关闭按钮
#     close_button = tk.Button(success_window, text="关闭", command=success_window.destroy)
#     close_button.pack(pady=10)
root.place_window_center()
root.resizable()
root.state()
frame = ttk.Frame()
frame.pack(pady=8)
input_va = ttk.StringVar()
ttk.Label(frame,text='输入要翻译的内容:',font=('微软雅黑',12)).pack(side=ttk.LEFT)
ttk.Entry(frame,textvariable=input_va).pack(side=ttk.LEFT,padx=5)
ttk.Button(frame,text='中英互译',command=show).pack(side=ttk.LEFT)
root.bind('<Return>', lambda event: show().invoke())
text_frame = ttk.Frame()
text_frame.pack()
ttk.Button(frame,text='中日互译',command=show1).pack(side=ttk.LEFT,padx=10)
style = ttk.Style()
style.configure("TButton", foreground="black", background="yellow")
ttk.Button(frame,text="朗读英语",command=read).pack(side=ttk.LEFT,padx=10,pady=20)
feedback_button = tk.Button(root, text="优化建议", command=show_feedback_window)
feedback_button.pack(side=tk.TOP, pady=10)
text = ttk.Text(text_frame)
text.pack()
root.mainloop()
