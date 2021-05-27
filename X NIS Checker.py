from tkinter import *
from tkinter.ttk import Combobox
import datetime

def show_res():
    try:
        global class_x
        global absen_x
        global result_print
        kelas_x = class_x.get().lower().split()
        kelas_x = ''.join(kelas_x)

        absen = int(absen_x.get())

        if kelas_x.isdigit() == True:
            result_print.config(text='Result : Please input class correctly! Example : X MIPA 1')
        
        elif kelas_x == 'xmipa1':
            data = []
            n = 202110001
            while n <= 202110035:
                data.append(n)
                n += 1
            result_print.config(text = 'Result : Your NIS is '+ str(data[absen-1]))

        elif kelas_x == 'xmipa2':
            data = []
            n = 202110036
            while n <= 202110071:
                data.append(n)
                n += 1
            result_print.config(text = 'Result : Your NIS is '+ str(data[absen-1]))
                    
        elif kelas_x == 'xmipa3':
            data = []
            n = 202110072
            while n <= 2021100107:
                data.append(n)
                n += 1
            result_print.config(text = 'Result : Your NIS is '+ str(data[absen-1]))
                    
        elif kelas_x == 'xmipa4':
            data = []
            n = 202110108
            while n <= 202110143:
                data.append(n)
                n += 1
            result_print.config(text = 'Result : Your NIS is '+ str(data[absen-1]))
                    
        elif kelas_x == 'xmipa5':
            data = []
            n = 202110144
            while n <= 202110179:
                data.append(n)
                n += 1
            result_print.config(text = 'Result : Your NIS is '+ str(data[absen-1]))
                    
        elif kelas_x == 'xmipa6':
            data = []
            n = 202110180
            while n <= 202110215:
                data.append(n)
                n += 1
            result_print.config(text = 'Result : Your NIS is '+ str(data[absen-1]))

        elif kelas_x == 'xmipa7':
            data = []
            n = 202110216
            while n <= 202110251:
                data.append(n)
                n += 1
            result_print.config(text = 'Result : Your NIS is '+ str(data[absen-1]))

        elif kelas_x == 'xmipa8':
            data = []
            n = 202110252
            while n <= 202110287:
                data.append(n)
                n += 1
            result_print.config(text = 'Result : Your NIS is '+ str(data[absen-1]))

        elif kelas_x == 'xips1':
            data = []
            n = 202110288
            while n <= 202110323:
                data.append(n)
                n += 1
            result_print.config(text = 'Result : Your NIS is '+ str(data[absen-1]))

        elif kelas_x == 'xips2':
            data = []
            n = 202110324
            while n <= 202110359:
                data.append(n)
                n += 1
            result_print.config(text = 'Result : Your NIS is '+ str(data[absen-1]))

        elif kelas_x == 'xips3':
            data = []
            n = 202110360
            while n <= 202110395:
                data.append(n)
                n += 1
            result_print.config(text = 'Result : Your NIS is '+ str(data[absen-1]))

        elif kelas_x == 'xips4':
            data = []
            n = 202110396
            while n <= 202110431:
                data.append(n)
                n += 1
            result_print.config(text = 'Result : Your NIS is '+ str(data[absen-1]))

        else:
            result_print.config(text = 'Result : There is no data! Please input again.')

    except IndexError:
        result_print.config(text= 'Result : Attendee\'s number is not more than 36! Please input again.')
    
    finally:
        x = datetime.datetime.now().strftime('%I:%M %p, %d/%m/%Y')
        date_time.config(text= 'Thank you for using this program\nYou access this program at '+x)

def delete():
    class_x.set('')
    absen_x.set('')
    date_time.config(text="")
    result_print.config(text="")

gui = Tk()
gui.geometry("450x300")
gui.iconbitmap('C:\\Users\\hp\\OneDrive\\Dokumen\\Python\\00-Template\\logo.ico')
gui.title('NIS Checker for 10th graders')
    
# the label for user_name
userclassLabel = Label(gui, text = "Class :").place(x = 40, y = 60)
data_class = (
    'X MIPA 1',
    'X MIPA 2',
    'X MIPA 3',
    'X MIPA 4',
    'X MIPA 5',
    'X MIPA 6',
    'X MIPA 7',
    'X MIPA 8',
    'X IPS 1',
    'X IPS 2',
    'X IPS 3',
    'X IPS 4',
)
class_x = Combobox(gui, values=data_class, width=10, state='readonly')
class_x.place(x = 110, y = 60)

# the label for user_password
userabsenLabel = Label(gui, text = "Number :").place(x = 40, y = 100)
data_absen = []
n = 1
while n <= 36:
    data_absen.append(n)
    n += 1
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
