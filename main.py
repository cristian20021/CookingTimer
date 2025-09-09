#TODO

# Connect the timers between themselves


import time
import pygame
from tkinter import *  
from tkinter import messagebox
from PIL import ImageTk, Image

B = Tk()
B.title("Countdown Timer")


B.geometry("400x400")

pygame.mixer.init()
pygame.mixer.music.load("soft_wake_up.mp3")


label = Label(B, text = "How many timers would you like to set?")
label.config(font =("Courier", 14))
label.pack()

# Number of timers input
nr_of_timers = Entry(B, font=("Helvetica", 14))
nr_of_timers.pack(pady=10)

class Timer():

    instances = []

    def __init__(self):
        self.time_set_by_user = 0
        self.timer_label = Label(B, text="00:00", font=("Helvetica", 48))
        self.time_left = 0
        Timer.instances.append(self)
        self.Status = False # reseted or not

    def reset_timer(self):
        pygame.mixer.music.stop()
        self.timer_label.config(text="00:00",fg='black')
        self.timer_label.config(text="00:00")
        self.Status = True
        self.time_left = 0
        

    def start_timer(self):
        self.Status = False
        
        print(self.time_set_by_user)
        try:
            self.time_left = self.time_set_by_user * 60  
            self.countdown()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

    def display_timer(self):
        spacing_header = Label(B, text = "--------------------------")
        spacing_header.config(font =("Courier", 14))
        spacing_header.pack()

        self.timer_label.pack()

        time_input = Entry(B, font=("Helvetica", 14))
        # time_input.insert(0,'Input minutes')
        time_input.pack(pady=10)

        setTimerButton = Button(B, text="Set Timer", font=("Helvetica", 14), command=lambda: self.updateTimer(time_input.get()))
        setTimerButton.pack( padx=20)
        

        start_button = Button(B, text="Start", font=("Helvetica", 14), command=self.start_timer)
        start_button.pack( padx=20)

        reset_button = Button(B, text="Reset", font=("Helvetica", 14), command=self.reset_timer)
        reset_button.pack( padx=20)



    def updateTimer(self,time_to_update):
        self.timer_label.config(text="00:00",fg='black')
        if int(time_to_update)>9:
            self.timer_label.config(text=f"{time_to_update}:00")
            
        else:
            self.timer_label.config(text=f"0{time_to_update}:00")

        self.time_set_by_user =  int(time_to_update )
        

    def countdown(self):
        print(type(self.time_left))
        if self.time_left > 0:
            mins, secs = divmod(self.time_left, 60)
            self.timer_label.config(text=f"{mins:02d}:{secs:02d}")
            self.time_left -= 1
            B.after(1000, self.countdown)  
        else:
            if self.Status != True:
                pygame.mixer.music.play()
            #messagebox.showinfo("Time's Up!", "The timer has finished.")
            self.timer_label.config(text="00:00",fg='red')
            
            
   
       


    @classmethod
    def start_all_timers(cls):
        for j in cls.instances:
            j.start_timer()



def proceed():



    for i in range(int(nr_of_timers.get())):
        timer = Timer()
        timer.display_timer()
    
        

    start_all_timers_button = Button(B, text="Start Together", font=("Helvetica", 14), command=Timer.start_all_timers)
    start_all_timers_button.pack( padx=20)
    





list_timers = Button(B, text="Proceed", font=("Helvetica", 14), command=proceed)
list_timers.pack(padx=20)


B.mainloop()