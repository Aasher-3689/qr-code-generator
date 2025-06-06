from tkinter import *
import qrcode

#---------CODE--------------------------------

def generate():
    text = getting_text_I.get(1.0, END)
    make_qr_code = qrcode.make(text)
    clear()
    make_qr_code.show()

#--------------------------
def clear():
    getting_text_I.delete(1.0, END)

#---------Tkinter-----------------------------

window = Tk()
window.resizable(False, False)
window.title("QR_CODE_GENERATOR_AASHER")
window.config(bg="#09071f")

#--------------------------
frame1 = Frame(window)
frame1.pack(side='top')
heading = Label(frame1, text="Universal QR Code Generator",
                font=('Roboto', 25), anchor='center',
                bg='#09071f', fg="#FFE873", relief="raised", bd=5,
                padx=14, pady=14)
heading.grid(row=0, column=0)

#--------------------------

frame2 = Frame(window)
frame2.pack(side='bottom')
footer = Label(frame2, text="© No rights reserved",
                font=('Arial', 11), anchor='center',
                bg='#16143d', fg="#c7c7c7",
                padx=215, pady=14)
footer.grid(row=0, column=0)

#--------------------------

frame3 = Frame(window)
frame3.pack(side='top')
getting_text_L = Label(frame3, text='Enter the text or paste the link below',
                     font=('Roboto', 18), anchor='center',
                     bg='#09071f', fg="#ffffff", pady=18)

getting_text_L.grid(row=0, column=0)

#---------------------------

frame4 = Frame(window)
frame4.pack(side='top')
getting_text_I = Text(frame4, font='Arial', bg='#16143d', fg="#c7c7c7",
                      width=50, height=10, relief='solid', padx=11, pady=10,
                      highlightbackground='#c7c7c7', highlightcolor='#7e6bed')

getting_text_I.grid(row=0, column=0)

#---------------------------

frame5 = Frame(window)
frame5.pack(side='top')
rough_label_1 = Label(frame5, bg='#09071f')
rough_label_1.grid(row=0, column=0)

frame6 = Frame(window)
frame6.pack(side='top')
generate_button = Button(frame6, text='Generate', bg='#09071f', fg='#7e6bed',
                         font=('Roboto', 14), relief='solid', padx=40,pady=5,
                         activebackground='#09071f', activeforeground='#c7c7c7',
                         command=generate, highlightbackground='#7e6bed')
generate_button.grid(row=0, column=0)

frame7 = Frame(window)
frame7.pack(side='top')
rough_label_2 = Label(frame7, bg='#09071f')
rough_label_2.grid(row=0, column=0)

#--------------------------
window.mainloop()
