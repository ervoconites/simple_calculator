import tkinter as tk
from calculator.simple_ui import *

window = tk.Tk()  # 创建主窗口对象
CalcPage(window)  # 创建计算器界面
window.mainloop()  # 启动tkinter主循环
