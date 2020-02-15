# ## Author : Lee Kang jin
# ## Description : Input - Location Type

import tkinter

def process_start():
    # main logic 실행
    count = 0

mainGUI = tkinter.Tk()



mainGUI.title("경매 데이터 분석")
mainGUI.geometry("400x200+0+0")

label = tkinter.Label(mainGUI, text="분석하고자 하는 주소를 입력하세요")
label.pack() 
text=tkinter.Text(mainGUI,height =3,width = 20)

text.pack()


btn1 = tkinter.Button(mainGUI, text="검색", command=process_start)
btn1.pack()




mainGUI.mainloop()

