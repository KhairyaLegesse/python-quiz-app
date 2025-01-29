import tkinter as tk  # Importing Tkinter for GUI
from tkinter import messagebox  # Importing messagebox for displaying alerts
import random  # Importing random module to select random questions

# Predefined quiz questions based on different topics
questions = {
    'Loops': [
        {
            'question': 'What is the output of the following code?\n\nfor i in range(3):\n    print(i)',
            'answer': '0 1 2',
            'options': ['0 1 2', '1 2 3', '0 1', '3 2 1']
        },
        {
            'question': 'How many times will the following loop execute?\n\nfor i in range(10, 20, 2):\n    print(i)',
            'answer': '5',
            'options': ['5', '10', '8', '7']
        }
    ],
    'Lists': [
        {
            'question': 'What is the result of the following code?\n\nlst = [1, 2, 3]\nprint(lst[1])',
            'answer': '2',
            'options': ['2', '1', '3', 'IndexError']
        },
        {
            'question': 'How do you add an element to the end of a list?\n\nlst = [1, 2, 3]',
            'answer': 'lst.append(4)',
            'options': ['lst.append(4)', 'lst.add(4)', 'lst.insert(4)', 'lst.extend(4)']
        }
    ]
}

# Initialize Tkinter root window
root = tk.Tk()  # Creating the main application window
root.title("Python Quiz App")  # Setting the title of the application window

# Global variables
current_question = None  # Variable to store the current question
options_var = tk.StringVar()  # StringVar to store the selected answer option

# Function to generate a question based on user input
def generate_question():
    global current_question  # Using global variable to store current question
    topic = topic_entry.get().strip()  # Getting the topic entered by the user and stripping any spaces

    if topic not in questions:  # Checking if the topic exists in predefined questions
        messagebox.showerror("Error", "Topic not found. Please try again.")  # Show error if topic is not found
        return
    
    current_question = random.choice(questions[topic])  # Select a random question from the chosen topic
    question_text.config(text=f"Topic: {topic}")  # Update the topic display label
    code_text.config(text=current_question['question'])  # Display the selected question

    # Clear previous options
    for widget in options_frame.winfo_children():  # Iterate through all existing radio buttons
        widget.destroy()  # Destroy old radio buttons

    options_var.set(None)  # Reset the selected option to None
    
    # Create new radio buttons for answer options
    for option in current_question['options']:
        rb = tk.Radiobutton(options_frame, text=option, variable=options_var, value=option)  # Create radio button
        rb.pack(anchor="w")  # Pack the radio button in the frame

# Function to check the user's answer
def check_answer():
    if options_var.get() == "":  # Check if the user has selected an answer
        messagebox.showwarning("Warning", "Please select an answer.")  # Show warning if no option is selected
        return
    
    if options_var.get() == current_question['answer']:  # Check if selected answer is correct
        feedback_label.config(text="Correct! Well done!", fg="green")  # Display success message
    else:
        feedback_label.config(text="Incorrect. Try again.", fg="red")  # Display failure message

# GUI Components
topic_label = tk.Label(root, text="Enter Python topic (e.g., Loops, Lists):")  # Label for topic input
topic_label.pack(pady=5)  # Pack the label with padding

topic_entry = tk.Entry(root, width=30)  # Entry field for topic input
topic_entry.pack(pady=5)  # Pack the entry field with padding

generate_button = tk.Button(root, text="Generate Python Question", command=generate_question)  # Button to generate question
generate_button.pack(pady=5)  # Pack the button with padding

question_text = tk.Label(root, text="Topic:", font=("Arial", 12, "bold"))  # Label to display topic
question_text.pack(pady=5)  # Pack the label with padding

code_text = tk.Label(root, text="", font=("Arial", 10))  # Label to display the question
code_text.pack(pady=5)  # Pack the label with padding

options_frame = tk.Frame(root)  # Frame to hold answer options
options_frame.pack(pady=5)  # Pack the frame with padding

submit_button = tk.Button(root, text="Submit", command=check_answer)  # Button to submit answer
submit_button.pack(pady=5)  # Pack the button with padding

feedback_label = tk.Label(root, text="", font=("Arial", 10, "italic"))  # Label to display feedback
feedback_label.pack(pady=5)  # Pack the label with padding

root.mainloop()  # Run the Tkinter event loop
