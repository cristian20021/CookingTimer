#TODO
# Set timer fix the zeros
# Connect the timers between themselves

from tkinter import *  
from tkinter import messagebox
from PIL import ImageTk, Image

B = Tk()
B.title("Countdown Timer")

# Set window size
B.geometry("400x400")

# Time variable


# canv = Canvas(B, width=400, height=400, bg='white')
# canv.grid(row=2, column=3)

# img = ImageTk.PhotoImage(Image.open("background.jpeg"))  # PIL solution
# canv.create_image(20, 20, anchor=NW, image=img)


# Timer label

label = Label(B, text = "How many timers would you like to set?")
label.config(font =("Courier", 14))
label.pack()

# Number of timers input
nr_of_timers = Entry(B, font=("Helvetica", 14))
nr_of_timers.pack(pady=10)

class Timer():

    def __init__(self):
        self.time_set_by_user = 0
        self.timer_label = Label(B, text="00:00", font=("Helvetica", 48))
        self.time_left = 0
    def reset_timer(self):
        
        self.timer_label.config(text="00:00")
        self.time_left = 0

    def start_timer(self):
        print(self.time_set_by_user)
        try:
            self.time_left = self.time_set_by_user * 60  
            self.countdown()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

    def display_timer(self):
        time_input = Entry(B, font=("Helvetica", 14))
        time_input.pack(pady=10)

        self.timer_label.pack()
        
        setTimerButton = Button(B, text="Set Timer", font=("Helvetica", 14), command=lambda: self.updateTimer(time_input.get()))
        setTimerButton.pack( padx=20)
        

        start_button = Button(B, text="Start", font=("Helvetica", 14), command=self.start_timer)
        start_button.pack( padx=20)

        reset_button = Button(B, text="Reset", font=("Helvetica", 14), command=self.reset_timer)
        reset_button.pack( padx=20)


        spacing = Label(B, text = "--------------------------")
        spacing.config(font =("Courier", 14))
        spacing.pack()


    def updateTimer(self,time_to_update):
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
            messagebox.showinfo("Time's Up!", "The timer has finished.")

    



def proceed():

    for i in range(int(nr_of_timers.get())):
        timer = Timer()
        timer.display_timer()
  


    # # global nr_of_timers 
    # for i in range(int(nr_of_timers.get())):
    #     timer_label = Label(B, text="00:00", font=("Helvetica", 48))
    #     timer_label.pack()

    #     # Time input entry
    #     time_input = Entry(B, font=("Helvetica", 14))
    #     time_input.pack(pady=10)
  
    #     start_button = Button(B, text="Start", font=("Helvetica", 14), command=start_timer)
    #     start_button.pack( padx=20)

    #     reset_button = Button(B, text="Reset", font=("Helvetica", 14), command=reset_timer)
    #     reset_button.pack( padx=20)




list_timers = Button(B, text="Proceed", font=("Helvetica", 14), command=proceed)
list_timers.pack(padx=20)


B.mainloop()