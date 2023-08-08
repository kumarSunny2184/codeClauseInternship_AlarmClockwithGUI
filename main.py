from tkinter import *
import datetime
import time
from pygame import mixer
import threading
from tkinter import messagebox

root = Tk()
root.title("Alarm Clock")
root.geometry("530x330")

alarmtime = StringVar()
msgi = StringVar()

head = Label(root, text="Alarm Clock", font=('comic sans', 20))
head.grid(row=0, columnspan=3, pady=10)

mixer.init()

def play_alarm():
    mixer.music.load('tone1.wav')  # Load a WAV audio file
    mixer.music.play()

def ala():
    target_time = datetime.datetime.strptime(alarmtime.get(), "%H:%M").time()

    def check_alarm():
        current_time = datetime.datetime.now().time()

        if current_time >= target_time:
            play_alarm()
            msg = messagebox.showinfo("Info", f'{msgi.get()}')
            mixer.music.stop()
        else:
            root.after(1000, check_alarm)  # Check again after 1 second

    check_alarm()  # Start checking

Clockimg = PhotoImage(file="al.png")

img = Label(root, image=Clockimg)
img.grid(rowspan=4, column=0)

inputt = Label(root, text="Input time", font=('comic sans', 18))
inputt.grid(row=1, column=1)

altime = Entry(root, textvariable=alarmtime, font=('comic sans', 18), width=6)
altime.grid(row=1, column=2)

msg = Label(root, text="Message", font=('comic sans', 18))
msg.grid(row=2, column=1, columnspan=2)

msginput = Entry(root, textvariable=msgi, font=('comic sans', 18))
msginput.grid(row=3, column=1, columnspan=2)

submit = Button(root, text="SUBMIT", font=('comic sans', 18), command=ala)  # Call the ala function when the button is clicked
submit.grid(row=4, column=1, columnspan=2)

root.mainloop()
