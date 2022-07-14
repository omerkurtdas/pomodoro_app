from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check_num = 0
timer = ""


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 == 0 and reps != 8:
        count_down(short_break_sec)
        label.config(text="BREAK", fg=PINK, bg=YELLOW, pady=25,
                     font=(FONT_NAME, 35, "bold"))
    elif reps % 2 == 1:
        count_down(work_sec)
        label.config(text="WORK", fg=GREEN, bg=YELLOW, pady=25,
                     font=(FONT_NAME, 35, "bold"))
    elif reps == 8:
        count_down(long_break_sec)
        label.config(text="BREAK", fg=RED, bg=YELLOW, pady=25,
                     font=(FONT_NAME, 35, "bold"))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if 0 <= count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        global check_num
        if reps % 2 == 0:
            check_num += 1
            label1 = Label()
            label1.config(text="✔", fg=GREEN, bg=YELLOW, pady=25, font=(FONT_NAME, 10, "bold"))
            #            label1.grid(row=3, column=1)
            label1.place(x=80 + check_num * 20, y=335)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# created canvas to place an image
canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_image)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# label for timer

label = Label()
label.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
label.grid(row=0, column=1)

# start button

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

# reset button

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
