import tkinter as tk
from tkinter import *

root=tk.Tk()
root.title('Enter Python topic')
Label(root,text='Enter Python topic').grid(row=5)
e1=Entry(root)
e1.grid(row=5,column=5)
root.mainloop()
questions = [
    {
        "topic": "Loops",
        "question": "What will be the output of this Python code?",
        "code": "for i in range(3):\n    print(i)",
        "options": ["0 1 2", "1 2 3", "0 1 2 3", "1 2"],
        "answer": 3 # Position in the options array 
    },
    {
        "topic": "Strings",
        "question": "What will be the output of this Python code?",
        "code": "s = 'hello'\nprint(s[1:4])",
        "options": ["ell", "hel", "llo", "h"],
        "answer": 0  # Position in the options array (0 corresponds to "ell")
    },
    {
        "topic": "Lists",
        "question": "What will be the output of this Python code?",
        "code": "lst = [1, 2, 3]\nprint(lst[1:])",
        "options": ["[2, 3]", "[1, 2, 3]", "[1, 2]", "IndexError"],
        "answer": 0  # Position in the options array (0 corresponds to "[2, 3]")
    }, 
    {
        "topic": "Dictionaries",
        "question": "What will be the output of this Python code?",
        "code": "d = {'a': 1, 'b': 2}\nprint(d['a'])",
        "options": ["1", "2", "KeyError", "None"],
        "answer": 0  # Position in the options array (0 corresponds to "1")
    },
    {
        "topic": "Functions",
        "question": "What will be the output of this Python code?",
        "code": "def add(a, b):\n    return a + b\nprint(add(2, 3))",
        "options": ["None", "23", "5", "TypeError"],
        "answer": 2  # Position in the options array (2 corresponds to "5")
    },

]









