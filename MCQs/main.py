#Python program to create a simple GUI
#Simple Quiz using tkinter

#import everything from tkinter
from tkinter import *

#import messagebox as mb from tkinter
from tkinter import messagebox as mb

#import json to use json file
import json

class Quiz:
    # This is the first method which is called when a
    # new object of the class is initialized. This method
    # sets the question count to 0. and initialize all the
    # other methoods to display the content and make all the
    # functionalities available
    def __init__(self):
        #set question to 0
        self.q_no = 0
        #assign ques to the display_question to update later
        self.display_title()
        self.display_question()
        #opt_selected holds an integer value which is used for selected option in a question
        self.opt_selected = IntVar()
        #displaying radio button for the current question and used to display options for the current question
        self.opts = self.radio_buttons()
        #display options for the next and exit
        self.display_options()
        #display the button for next and exit
        self.buttons()
        #no of questions
        self.data_size = len(question)
        #keep a counter of correct answers
        self.correct = 0
        
    #This method is used to display the result
    #It counts the number of correct and wrong asnwers
    # and then displays them at the end as a message box
    def display_result(self):
        #calculates the wrong count
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"
        #calculates the percentage of correct answers
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"
        #Shows a message box to display the result
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")
        
    def check_ans(self, q_no):
        #Check for if the selected o[tions is correct
        if self.opt_selected.get() == answer[q_no]:
            return True
    
    #This method is used to check the answer of the currect question by calling the check_ans and question no.
    def next_btn(self):
        #check if the answer is correct
        if self.check_ans(self.q_no):
            #if the anseer is correct it increments the correct vy 1
            self.correct += 1
        #moves to next question by incrementing the q_no counter
        self.q_no += 1
        #check if the q_no size is equal to the data size
        if self.q_no == self.data_size:
            #if it is correct then it displays the score
            self.display_result()
            #destroy the gui
            gui.destroy()
        else:
            #shows the next question
            self.display_question()
            self.display_options()
    
    #This method shows the two buttons on the screen.
    def buttons(self):
        #the first button is the next button to move to the next question
        next_button = Button(gui, text="Next", command=self.next_btn, width=10, bg="blue", fg="white", font=("ariel",16,"bold"))
        #placing the button on the screen
        next_button.place(x=350, y=380)
        #this is the second button which is used to Quit the GUI
        quit_button = Button(gui, text="Quit", command=gui.destroy, width=5, bg="black", fg="white", font=("ariel",16,"bold"))
        #placing the quit button on the screen
        quit_button.place(x = 700, y = 50)
    
    #this method deselect the radio button on the screen
    def display_options(self):
        val = 0
        #deselecting the options
        self.opt_selected.set(0)
        #looping over the options to be displayed for the text of the radio button
        for option in options[self.q_no]:
            self.opts[val]['text'] = option
            val+=1
    
    #this method shows the current question on the screen
    def display_question(self):
        #setting the question properties
        q_no = Label(gui, text=question[self.q_no], width=50, font=('ariel', 16, 'bold'), anchor='w')
        #placing the option on the screen
        q_no.place(x=70, y=100)
    #this method is used to display title
    def display_title(self):
        # the title to be shown
        title = Label(gui, text="MCQ Quiz",width=60, bg="green", fg="white", font=("ariel", 16, "bold"))
        #place of the title
        title.place(x=0, y=2)
    
    #this method shows the radio buttons to select the questions on the screen at the specified position.
    def radio_buttons(self):
        #initialize the list with an emoty list of options
        q_list = []
        #position of the first option
        y_pos = 150
        #adding the options to the list
        while len(q_list) < 4:
            #setting the radio button properties
            radio_btn = Radiobutton(gui, text=" " , variable=self.opt_selected, value= len(q_list)+1, font=("ariel",14))
            #adding the button to the list
            q_list.append(radio_btn)
            #placing the button
            radio_btn.place(x=100, y=y_pos)
            #incrementing the y-axis position by 40
            y_pos += 40
        return q_list
    



# create a gui window
gui = Tk()

#set the size of the gui window
gui.geometry("785x450")

#Set the title of the window
gui.title("MCQ Quiz")

#get the data from the json file
with open('data.json') as f:
    data = json.load(f)

#set the question, options, and answer
question = (data['question'])
options = (data['options'])
answer = (data['answer'])

#create a object of the Quiz Class
quiz = Quiz()

#Start the GUI
gui.mainloop()

#END OF THE PROGRAM