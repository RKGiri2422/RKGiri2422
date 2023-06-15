import tkinter as tk
from datetime import datetime, timedelta

counter = timedelta(hours=0, minutes=0, seconds=0)
running = False
lap_times = []


def counter_label(label):
    def count():
        if running:
            global counter

            if counter == timedelta(hours=0, minutes=0, seconds=0):
                display = "00:00:00"
            else:
                display = str(counter)

                if len(display) < 8:
                    display = "0" + display

            label['text'] = display

            label.after(1000, count)
            counter += timedelta(seconds=1)

    count()


def start(label):
    global running
    running = True
    counter_label(label)
    start_button['state'] = 'disabled'
    stop_button['state'] = 'normal'
    reset_button['state'] = 'normal'
    lap_button['state'] = 'normal'


def stop():
    global running
    running = False
    start_button['state'] = 'normal'
    stop_button['state'] = 'disabled'


def reset(label, listbox):
    global counter, lap_times
    counter = timedelta(hours=0, minutes=0, seconds=0)
    lap_times = []

    if not running:
        start_button['state'] = 'normal'
        stop_button['state'] = 'disabled'
        reset_button['state'] = 'disabled'
        lap_button['state'] = 'disabled'
        label['text'] = '00:00:00'
    else:
        label['text'] = 'Starting...'

    listbox.delete(0, tk.END)


def lap(label, listbox):
    global counter, lap_times
    if running:
        lap_time = counter
        lap_times.append(lap_time)
        display = str(lap_time)

        if len(display) < 8:
            display = "0" + display

        lap_num = len(lap_times)
        listbox.insert(tk.END, f"{lap_num}. {display}")


root = tk.Tk()
root.title("Stopwatch")

root.minsize(width=250, height=200)
label = tk.Label(root, text="00:00:00", fg="black", font="Verdana 30 bold")
label.pack()

frame = tk.Frame(root)
frame.pack(pady=5)

start_button = tk.Button(frame, text='Start', width=6, command=lambda: start(label))
stop_button = tk.Button(frame, text='Stop', width=6, state='disabled', command=stop)
reset_button = tk.Button(frame, text='Reset', width=6, state='disabled', command=lambda: reset(label, lap_listbox))
lap_button = tk.Button(frame, text='Lap', width=6, state='disabled', command=lambda: lap(label, lap_listbox))

start_button.pack(side="left")
stop_button.pack(side="left")
reset_button.pack(side="left")
lap_button.pack(side="left")

lap_frame = tk.Frame(root)
lap_frame.pack(pady=5)

lap_listbox = tk.Listbox(lap_frame, font=("Arial", 12), width=15)
lap_listbox.pack()

root.mainloop()
