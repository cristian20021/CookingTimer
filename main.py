import time
import pygame
from tkinter import *  
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image

B = Tk()
B.title("Countdown Timer")
B.geometry("350x600")

pygame.mixer.init()
pygame.mixer.music.load("soft_wake_up.mp3")


main_frame = Frame(B)
main_frame.pack(fill=BOTH, expand=1)

canvas = Canvas(main_frame)
canvas.pack(side=LEFT, fill=BOTH, expand=1)

scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

content_frame = Frame(canvas)

canvas.create_window((0, 0), window=content_frame, anchor="nw")


def _on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

canvas.bind_all("<MouseWheel>", _on_mousewheel)


label = Label(content_frame, text = "How many timers would you like to set?")
label.config(font =("Courier", 14))
label.pack()

# Number of timers input
nr_of_timers = Entry(content_frame, font=("Helvetica", 14))
nr_of_timers.pack(pady=10)

class Timer():

    instances = []

    def __init__(self):
        self.time_set_by_user = 0
        self.timer_label = Label(content_frame, text="00:00", font=("Helvetica", 48))
        self.time_left = 0
        Timer.instances.append(self)
        self.Status = False # reseted or not
        self.Paused = False # has it been paused or not for resuming or starting
        self.Started = False # has it started for multiple timer set ups
    
    def reset_timer(self):
        pygame.mixer.music.stop()
        self.timer_label.config(text="00:00",fg='black')
        self.timer_label.config(text="00:00")
        self.Status = True
        self.time_left = 0

        
    def pause_timer(self):
        self.Paused = True
        self.countdown()


    def start_timer(self):
        if self.Paused == True:
            self.Paused = False
        self.Status = False
   
        print(self.time_set_by_user)
        try:
                if self.Started == False:
                    self.time_left = self.time_set_by_user * 60  
                    self.countdown()
                    self.Started = True
                else:
                    self.countdown()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

    def display_timer(self):
        spacing_header = Label(content_frame, text = "--------------------------")
        spacing_header.config(font =("Courier", 14))
        spacing_header.pack()

        self.timer_label.pack()

        time_input = Entry(content_frame, font=("Helvetica", 14))
        # time_input.insert(0,'Input minutes')
        time_input.pack(pady=10)

        setTimerButton = Button(content_frame, text="Set Timer", font=("Helvetica", 14), command=lambda: self.updateTimer(time_input.get()))
        setTimerButton.pack( padx=20)
        
        

        start_button = Button(content_frame, text="Start", font=("Helvetica", 14), command=self.start_timer)
        start_button.pack( padx=20)

        start_button = Button(content_frame, text="Pause", font=("Helvetica", 14), command=self.pause_timer)
        start_button.pack( padx=20)

        reset_button = Button(content_frame, text="Reset", font=("Helvetica", 14), command=self.reset_timer)
        reset_button.pack( padx=20)

        # Update canvas scroll region after adding widgets
        content_frame.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))



    def updateTimer(self,time_to_update):
        self.timer_label.config(text="00:00",fg='black')
        if int(time_to_update)>9:
            self.timer_label.config(text=f"{time_to_update}:00")
            
        else:
            self.timer_label.config(text=f"0{time_to_update}:00")

        self.time_set_by_user =  int(time_to_update )
        

    def countdown(self):
        
            print(self.time_left)
            
            if self.time_left > 0 and self.Paused == False:
                mins, secs = divmod(self.time_left, 60)
                self.timer_label.config(text=f"{mins:02d}:{secs:02d}")
                self.time_left -= 1
                B.after(1000, self.countdown)  
            elif self.Paused == True:
                mins, secs = divmod(self.time_left, 60)
                self.timer_label.config(text=f"{mins:02d}:{secs:02d}")
            else:
                if self.Status != True:
                    pygame.mixer.music.play()
                #messagebox.showinfo("Time's Up!", "The timer has finished.")
                self.timer_label.config(text="00:00",fg='red')
                self.Started = False
                print(f'Status:{self.Status}, Pause:{self.Paused}, Started:{self.Started}')
                
      
            
   
       


    @classmethod
    def start_all_timers(cls):
        for j in cls.instances:
            j.start_timer()


def proceed():
    start_all_timers_button = Button(content_frame, text="Start Together", font=("Helvetica", 14), command=Timer.start_all_timers)
    start_all_timers_button.pack( padx=20)
    for i in range(int(nr_of_timers.get())):
        timer = Timer()
        timer.display_timer()
    

    
   
    content_frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))

list_timers = Button(content_frame, text="Proceed", font=("Helvetica", 14), command=proceed)
list_timers.pack(padx=20)

B.mainloop()