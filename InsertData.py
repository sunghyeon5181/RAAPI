# ## Author : Lee Kang jin
# ## Description : Input - Location Type

import tkinter 
from tkinter import messagebox
import GetRealEstateTradeData as gt

def process_start():
    inputText = text.get("1.0","end")
    inputTextParsing = str(inputText).split(' ')

    response_body = gt.GetRealEstateTradeData.getCode(inputTextParsing[0].encode('utf-8') , inputTextParsing[1].encode('utf-8') )
    print(response_body)

    
mainGUI = tkinter.Tk()

mainGUI.title("경매 데이터 분석")
mainGUI.geometry("400x200+0+0")

label = tkinter.Label(mainGUI, text="주소를 입력:")

# label.grid(row=0, column=0)
label.pack() 

text = tkinter.Text(mainGUI,height =1,width = 20)
# text.grid(row =0, colum = 1)
text.pack()


btnSearch = tkinter.Button(mainGUI, text="완료", command=process_start)
# btnSearch.grid(row =1, colum =1)
btnSearch.pack()


mainGUI.mainloop()


