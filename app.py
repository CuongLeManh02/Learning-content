import tkinter as tk
from PIL import Image, ImageTk
import cv2
import imutils
print("Phần mềm đang chạy...")

v = tk.Tk()
v.geometry ("700x700+200+10")
v.title("Nhận Dạng Ngôn Ngữ Ký Hiệu")
v.resizable(width=False, height=False)
f = tk.PhotoImage(file="images.png")
f1 = tk.Label(v, image = f).place(x=0, y=0,relwidth=1, relheight=1)
def login():
        import signlanguage
        log =signlanguage
tk.Label(v,text="Phần mềm Biên dịch ngôn ngữ ký hiệu",font="lucida 20 bold").place(x=90,y=10)
tk.Button(v,fg='white',bg='green',border=0 ,text='MỞ CAMERA',width ='20',height='2',font =('time new roman',10),command=login ).place(x=265,y=620)
       
v.mainloop()