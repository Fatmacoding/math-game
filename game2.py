import tkinter as tk
from tkinter import StringVar
import ttkbootstrap as tb
# root = tk.Tk()
root=tb.Window(themename="superhero")
root.title("Math game")
root.geometry('520x550')

class TimerApp:
    def __init__(self, master):
        self.master = master
        self.time_label = tk.Label(master, text="0",fg="#FFFFF0", font=('Verdana', 20),wraplength=500)
        self.time_label.grid(row=0,column=0,pady=2)
        self.timer_running = False
        self.seconds = 0

    def start_timer(self):
        self.timer_running = True
        self.update_timer()

    def stop_timer(self):
        self.timer_running = False
        self.seconds = 0

    def update_timer(self):
        if self.timer_running:
            self.seconds += 1
            self.time_label.config(text="Time : " + str(self.seconds)+"s")
            self.master.after(1000, self.update_timer)


questions = [
            "4 X 5 = ?",
            "9 X 6 = ?",
            "9 X 4 = ?",
            "2 X 4 = ?",
            "8 X 6 = ?",
            "4 X 4 = ?" 
            ]

options = [ 
            ['23','20','34','9','20'],
            ['88','34','54','60','54'],
            ['55','36','33','57','36'],
            ['8','5','9','34','8'],
            ['29','48','24','12','48'],
            ['14','19','15','16','16']
        ]


frame = tk.Frame(root, padx=10, pady=10, bd=8, relief="groove")
question_label = tk.Label(frame,height=5, width=28,font=('Verdana', 20),wraplength=500, bd=4, relief="groove")

question_label["bg"] = '#C0C0C0'
question_label["fg"]="#0047AB"


v1 = StringVar(frame)
v2 = StringVar(frame)
v3 = StringVar(frame)
v4 = StringVar(frame)

option1 = tk.Radiobutton(frame, bg="#fff", variable=v1, font=('Verdana', 20), command = lambda : checkAnswer(option1))
option2 = tk.Radiobutton(frame, bg="#fff", variable=v2, font=('Verdana', 20), command = lambda : checkAnswer(option2))
option3 = tk.Radiobutton(frame, bg="#fff", variable=v3, font=('Verdana', 20), command = lambda : checkAnswer(option3))
option4 = tk.Radiobutton(frame, bg="#fff", variable=v4, font=('Verdana', 20), command = lambda : checkAnswer(option4))

button_next =  tb.Button(frame , text='Next' ,bootstyle="secondary",width=40, command= lambda : displayNextQuestion())

frame.pack(fill="both", expand="true")
app = TimerApp(frame)
question_label.grid(row=1, column=0,pady=5)

option1.grid(sticky= 'W', row=2, column=0,pady=5)
option2.grid(sticky= 'W', row=3, column=0,pady=5)
option3.grid(sticky= 'W', row=4, column=0,pady=5)
option4.grid(sticky= 'W', row=5, column=0,pady=5)

button_next.grid(pady=10)


index = 0
correct = 0

# create a function to disable radiobuttons
def disableButtons(state):
    option1['state'] = state
    option2['state'] = state
    option3['state'] = state
    option4['state'] = state


# create a function to check the selected answer
def checkAnswer(radio):
    global correct, index

    if radio['text'] == options[index][4]:
        correct +=1

    index +=1
    disableButtons('disable')


# create a function to display the next question
def displayNextQuestion():
    global index, correct



    if button_next['text'] == 'Restart The game':
        correct = 0
        index = 0
        button_next['text'] = 'Next'
        question_label["bg"] = '#C0C0C0'
        question_label["fg"]="#0047AB"
        

    if index == len(options):
       question_label['text'] = str(correct) + " / " + str(len(options))
       button_next['text'] = 'Restart The game'

       if correct >= len(options)/2:
            question_label['bg'] = '#556B2F'
            question_label["fg"]="#fff"
            app.stop_timer()
       else:
            question_label['bg'] = '#8B0000'
            question_label["fg"]="#FFFFF0"
            app.stop_timer()

    else:
        app.start_timer()
        question_label['text'] = questions[index]        
        disableButtons('normal')
        opts = options[index]
        option1['text'] = opts[0]
        option2['text'] = opts[1]
        option3['text'] = opts[2]
        option4['text'] = opts[3]
        v1.set(opts[0])
        v2.set(opts[1])
        v3.set(opts[2])
        v4.set(opts[3])

        if index == len(options) - 1:
            button_next['text'] = 'Check the Results'


displayNextQuestion()
root.mainloop()