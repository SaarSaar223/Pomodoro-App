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
REPS = 0
timer1 = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global REPS
    window.after_cancel(timer1)
    REPS = 0
    label_one.config(text = "Timer")
    canvas.itemconfig(clock, text = "00:00")
    label_two.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1
    if(REPS % 8 == 0):
        label_one.config(text = "LONG BREAK", fg = RED)
        timer(LONG_BREAK_MIN*60)
    elif (REPS % 2 == 1):
        label_one.config(text = "WORK", fg = PINK)
        timer(WORK_MIN*60)
    else:
        label_one.config(text = "SHORT BREAK", fg = GREEN)
        timer(SHORT_BREAK_MIN*60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def timer(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0" + str(count_sec)

    canvas.itemconfig(clock, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer1
        timer1 = window.after(1000, timer, count-1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(REPS/2)):
            mark += "✓"

        label_two.config(text = mark)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady=50, bg = YELLOW)


canvas = Canvas(width=200, height=224, bg = YELLOW, highlightthickness = 0)
tomatoimg = PhotoImage(file = "tomato.png")
canvas.create_image(100,112, image=tomatoimg)
clock = canvas.create_text(100, 130, text="00:00", fill="white", font = (FONT_NAME,35, "bold"))
canvas.grid(row = 1, column = 1)


label_one = Label(text = "Timer", fg = GREEN, bg = YELLOW,font = (FONT_NAME, 45, "bold"))
label_one.grid(row = 0, column = 1)

button_one = Button(text = "Start", command = start_timer)
button_one.grid(row=3, column=0)

button_two = Button(text = "Reset", command = reset)
button_two.grid(row=3, column=2)

label_two = Label(text = "", fg = GREEN, bg = YELLOW,font = (FONT_NAME, 10, "bold"))
label_two.grid(row = 4, column = 1)

window.mainloop()