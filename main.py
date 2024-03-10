from tkinter import *
import math
import winsound

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✔"
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    # noinspection PyTypeChecker
    window.after_cancel(timer)
    my_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        winsound.Beep(440, 1000)  # A beep at 440 Hz for 1 second
        count_down(long_break_sec)
        my_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        winsound.Beep(440, 1000)  # A beep at 440 Hz for 1 second
        count_down(short_break_sec)
        my_label.config(text="Break", fg=PINK)
    else:
        winsound.Beep(440, 1000)  # A beep at 440 Hz for 1 second
        count_down(work_sec)
        my_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

### chemand functia pe sine o sa ia argumentul pe care il bagi adica un nr si cand se cheama pe sine o sa ia argument
# numarul respectiv minus 1.
def count_down(count):
    ### math.floor va rotunjii numarul la urmatorul cel mai mic numar intreg.
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sesions = math.floor(reps / 2)
        for _ in range(work_sesions):
            marks += "✔"
        check.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

## Canvas:
canvas = Canvas(window, width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img, )
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Labels:

my_label = Label(window, text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
my_label.grid(column=1, row=0)

check = Label(window, font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
check.grid(column=1, row=4)

# Buttons:

start_button = Button(window, text="Start", font=(FONT_NAME, 10, "bold"), command=start_timer)
start_button.grid(column=0, row=3)

reset_button = Button(window, text="Reset", font=(FONT_NAME, 10, "bold"), command=reset_timer)
reset_button.grid(column=2, row=3)

window.mainloop()
