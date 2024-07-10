# import tkinter as tk
# from tkinter import ttk
#
# # 创建主窗口
# root = tk.Tk()
# root.title("ttk 示例")
#
# # 创建一个按钮，点击时会执行回调函数
# def on_button_click():
#     print("按钮被点击了")
# button = ttk.Button(root, text="点击我", command=on_button_click)
# button.pack()
#
# # 创建一个标签
# label = ttk.Label(root, text="这是一个标签")
# label.pack()
#
# # 创建一个文本输入框
# entry = ttk.Entry(root)
# entry.pack()
#
# # 创建一个下拉选择框
# combo = ttk.Combobox(root, values=["选项1", "选项2", "选项3"])
# combo.pack()
#
# # 创建一个复选框
# check = ttk.Checkbutton(root, text="选择我")
# check.pack()
#
# # 创建两个单选按钮
# radio_var = tk.IntVar()  # 用于关联单选按钮的变量
# radio1 = ttk.Radiobutton(root, text="选项A", value=1, variable=radio_var)
# radio2 = ttk.Radiobutton(root, text="选项B", value=2, variable=radio_var)
# radio1.pack()
# radio2.pack()
#
# # 创建一个数字选择框
# spin = ttk.Spinbox(root, from_=0, to=10)
# spin.pack()
#
# # 创建一个树形视图，用于显示表格数据
# tree = ttk.Treeview(root, columns=("列1", "列2"))
# tree.pack()
#
# # 创建一个标签页控件
# notebook = ttk.Notebook(root)
# tab1 = ttk.Frame(notebook)
# tab2 = ttk.Frame(notebook)
# notebook.add(tab1, text="标签页1")
# notebook.add(tab2, text="标签页2")
# notebook.pack()
#
# # 定制按钮的样式
# style = ttk.Style()
# style.configure("TButton", foreground="blue", background="yellow")
#
# # 运行主循环
# root.mainloop()




# import tkinter as tk
# from tkinter import ttk
#
# def search():
#     # 这里添加你的搜索逻辑
#     print("搜索：", entry.get())
#
# # 创建主窗口
# root = tk.Tk()
# root.title("搜索框")
#
# # 创建一个标签
# label = ttk.Label(root, text="请输入搜索内容：")
# label.pack(pady=10)
#
# # 创建一个文本输入框
# entry = ttk.Entry(root, width=50)
# entry.pack(padx=10, pady=10)
#
# # 创建搜索按钮，并绑定到search函数
# search_button = ttk.Button(root, text="搜索", command=search)
# search_button.pack(pady=10)
#
# # 绑定回车键到搜索按钮的功能
# root.bind('<Return>', lambda event: search_button.invoke())
#
# # 启动事件循环
# root.mainloop()



import tkinter as tk
from tkinter import ttk

def show_feedback_window():
    feedback_window = tk.Toplevel(root)
    feedback_window.title("反馈建议")
    feedback_window.geometry("400x200")  # 可以设置一个初始大小

    # 创建一个文本框供用户输入反馈内容
    feedback_text = tk.Text(feedback_window, height=10)
    feedback_text.pack(pady=10)

    # 创建一个提交按钮，点击后关闭反馈窗口
    submit_button = tk.Button(feedback_window, text="提交", command=feedback_window.destroy)
    submit_button.pack(pady=10)

# 你的其他代码保持不变

# 在你的应用程序主循环中添加反馈按钮
feedback_button = tk.Button(root, text="反馈建议", command=show_feedback_window)
feedback_button.pack(side=tk.BOTTOM, pady=10)

root.mainloop()
