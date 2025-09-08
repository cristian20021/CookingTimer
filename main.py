from tkinter import *  
from tkinter import messagebox


B = Tk()
B.title("Countdown Timer")

# Set window size
B.geometry("400x400")

# Time variable
time_left = 0


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
     
    def reset_timer(self):
        global time_left
        time_left = 0
        self.timer_label.config(text="00:00")
        self.time_input.delete(0, END)

    def start_timer(self,time_set_by_user):
            
        global time_left
        try:
            time_left = int(time_set_by_user.get()) * 60  
            self.countdown()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

    def display_timer(self):

        self.timer_label.pack()
        

        start_button = Button(B, text="Start", font=("Helvetica", 14), command=self.start_timer)
        start_button.pack( padx=20)

        reset_button = Button(B, text="Reset", font=("Helvetica", 14), command=self.reset_timer)
        reset_button.pack( padx=20)

    def countdown(self):
        global time_left
        if time_left > 0:
            mins, secs = divmod(time_left, 60)
            self.timer_label.config(text=f"{mins:02d}:{secs:02d}")
            time_left -= 1
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