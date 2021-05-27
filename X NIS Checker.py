from tkinter import *
from tkinter.ttk import Combobox
import datetime

def datetimes():
    x = datetime.datetime.now().strftime('%I:%M %p, %d/%m/%Y')
    date_time.config(text= 'Thank you for using this program\nYou access this program at '+x)

def show_res():
    global result_print
    kelas = ''.join(kelas_x.get().lower().split())

    absen = int(absen_x.get())

    if kelas == 'xmipa1':
        if absen == 36:
            result_print.config(text='Result : X MIPA 1 just has 35 students!')
            datetimes()
        else:
            data = list(range(202110001, 202110036))
            result_print.config(text = 'Result : Your NIS is '+ str(data[absen-1]))
            datetimes()

    elif kelas == 'xmipa2':
        data = list(range(202110036, 202110072))
        result_print.config(text = 'Result : Your NIS is '+ str(data[absen-1]))
        datetimes()
                
    elif kelas == 'xmipa3':
        data = list(range(202110072, 202110108))
        result_print.config(text = 'Result : Your NIS is '+ str(data[absen-1]))
        datetimes()
                
    elif kelas == 'xmipa4':
        data = list(range(202110108, 202110144))
        result_print.config(text = 'Result : Your NIS is '+ str(data[absen-1]))
        datetimes()
                
    elif kelas == 'xmipa5':
        data = list(range(202110144, 202110180))
        result_print.config(text = 'Result : Your NIS is '+ str(data[absen-1]))
        datetimes()
                
    elif kelas == 'xmipa6':
        data = list(range(202110180, 202110216))
        result_print.config(text = 'Result : Your NIS is '+ str(data[absen-1]))
        datetimes()

    elif kelas == 'xmipa7':
        data = list(range(202110216, 202110252))
        result_print.config(text = 'Result : Your NIS is '+ str(data[absen-1]))
        datetimes()

    elif kelas == 'xmipa8':
        data = list(range(202110252, 202110288))
        result_print.config(text = 'Result : Your NIS is '+ str(data[absen-1]))
        datetimes()

    elif kelas == 'xips1':
        data = list(range(202110288, 202110324))
        result_print.config(text = 'Result : Your NIS is '+ str(data[absen-1]))
        datetimes()

    elif kelas == 'xips2':
        data = list(range(202110324, 202110360))
        result_print.config(text = 'Result : Your NIS is '+ str(data[absen-1]))
        datetimes()

    elif kelas == 'xips3':
        data = list(range(202110360, 202110396))
        result_print.config(text = 'Result : Your NIS is '+ str(data[absen-1]))
        datetimes()

    elif kelas == 'xips4':
        data = list(range(202110396, 202110432))
        result_print.config(text = 'Result : Your NIS is '+ str(data[absen-1]))
        datetimes()

def delete():
    kelas_x.set('')
    absen_x.set('')
    date_time.config(text="")
    result_print.config(text="")

gui = Tk()
gui.geometry("450x300")
gui.title('NIS Checker for 10th graders')
    
# the label for user_name
userclassLabel = Label(gui, text = "Class :").place(x = 40, y = 60)
data_class = ('X MIPA 1','X MIPA 2','X MIPA 3','X MIPA 4','X MIPA 5','X MIPA 6',
              'X MIPA 7','X MIPA 8','X IPS 1','X IPS 2','X IPS 3','X IPS 4')
kelas_x = Combobox(gui, values=data_class, width=10, state='readonly')
kelas_x.place(x = 110, y = 60)

# the label for user_password
userabsenLabel = Label(gui, text = "Number :").place(x = 40, y = 100)
data_absen = list(range(1,37))
absen_x = Combobox(gui,values=data_absen, width = 10, state='readonly')
absen_x.place(x = 110, y = 100)

# the label for result
result_print = Label(gui)
result_print.place(x = 40, y= 180)

# date time
date_time = Label(gui, justify=LEFT, anchor='w')
date_time.place(x = 40, y= 210)

# quit button
quitbutton = Button(gui, text="Quit", command=gui.destroy, width=5).place(x= 40, y = 140)
# Result button generator
submitbutton = Button(gui, text = "Submit", command=show_res).place(x = 110, y = 140)
# clear button
clearbutton = Button(gui, text="Clear", command=delete).place(x = 180, y = 140)
    
# start program
gui.mainloop()
