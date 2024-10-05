'''Exercise 1: User Input and Conditional Statements
Write a program that asks the user for a number of then prints the following sentence that number of times:
‘I am back to check on my skills!’ If the number is greater than 10, print this sentence instead:
‘Python conditions and loops are a piece of cake.’ Assume you can only pass positive integers.
'''

# User Input and Conditional Statements
# inputs: An integer
# output: Repeated sentence by users input integer times

#Steps:
# . create GUI
# . start
# . read the number from the user
# . compare user int to 10 if it's less than 10 & > 0 output = ‘I am back to check on my skills!’ printed int times
#    if int < 10 output= ‘Python conditions and loops are a piece of cake.’.

import tkinter as tk
import sys

# Rendering the output of the function on TK window
import tkinter as tk
import sys


class RedirectText(object):
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, string):
        self.text_widget.insert(tk.END, string)
        self.text_widget.see(tk.END)

    def flush(self):
        pass


def create_window():
    global win, text_widget

    win = tk.Tk()
    win.title("Auto Message App")
    win.geometry("500x150")
    win.configure(bg="lightblue")

    text_widget = tk.Text(win, wrap='word', height=15, width=50, bg="lightblue", font=("Arial", 20,"bold"))
    text_widget.pack(pady=30)

    sys.stdout = RedirectText(text_widget)

    showMessages()


def showMessages():
    messages = [
        " لا اله الا الله محمد رسول الله",
        "اللهم لا اله الا انت سبحانك انى كنت من الظالمين",
        "سبحان الله وبحمده سبحان الله العظيم",
        "لا حول ولا قوة الا بالله",
        "الحمدلله"
    ]

    def display_message(index):
        if index < len(messages):
            text_widget.delete(1.0, tk.END)  # Clear the text widget
            print(messages[index])
            win.after(12000, lambda: display_message(index + 1))  # Show next message after 12 seconds
        else:
            win.after(12000, close_window)  # Close window after the last message

    display_message(0)


def close_window():
    win.destroy()
    win.after(900000, create_window)  # Reopen window after 15 minutes


# Start the application
create_window()

tk.mainloop()
