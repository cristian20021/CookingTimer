from tkinter import *  
from tkinter import messagebox


B = Tk()
B.title("Countdown Timer")

# Set window size
B.geometry("300x200")

# Time variable
time_left = 0

# Timer label

#nr_of_timers = input("How many timers would you like to add?")

label = Label(B, text = "Fact of the Day")
label.config(font =("Courier", 14))
label.pack()

timer_label = Label(B, text="00:00", font=("Helvetica", 48))
timer_label.pack()

# Time input entry
time_input = Entry(B, font=("Helvetica", 14))
time_input.pack(pady=10)

def start_timer():
    global time_left
    try:
        time_left = int(time_input.get()) * 60  
        countdown()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

def countdown():
    global time_left
    if time_left > 0:
        mins, secs = divmod(time_left, 60)
        timer_label.config(text=f"{mins:02d}:{secs:02d}")
        time_left -= 1
        B.after(1000, countdown)  
    else:
        messagebox.showinfo("Time's Up!", "The timer has finished.")

def reset_timer():
    global time_left
    time_left = 0
    timer_label.config(text="00:00")
    time_input.delete(0, END)


start_button = Button(B, text="Start", font=("Helvetica", 14), command=start_timer)
start_button.pack(side="left", padx=20)

reset_button = Button(B, text="Reset", font=("Helvetica", 14), command=reset_timer)
reset_button.pack(side="right", padx=20)

B.mainloop()