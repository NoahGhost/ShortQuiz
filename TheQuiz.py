import tkinter as tk
from tkinter import messagebox, ttk, PhotoImage
from ttkbootstrap import Style
from quiz import quiz
from PIL import Image, ImageTk

# Function to display the current question and choices
def show_question():
    # Get the current question from quiz
    question = quiz[current_question]
    question_label.config(text=question["question"])

    # Display the choices on the buttons
    choices = question["choices"]
    for i in range(4):
        choice_btns[i].config(text=choices[i], state="normal") #reset button's state

    # Clear the feedback label and disable the next button
    feedback_label.config(text="")
    next_btn.config(state="disabled")

# Function to check the selected answer and provide feedback
def check_answer(choice):
    # Get the current question from quiz
    question = quiz[current_question]
    selected_choice = choice_btns[choice].cget("text")

    # Check if the selected choice is correct
    if selected_choice == question["answer"]:
        global score 
        score += 1
        score_label.config(text="{}/{}".format(score, len(quiz)))
        feedback_label.config(text="Correct!", foreground="black", background="#5EE651")
    else:
        feedback_label.config(text="Eh! Wrong!", foreground="black", background="#C75B52")

    # Disable the choice buttons and enable the next button
    for btn in choice_btns:
        btn.config(state="disabled")
    next_btn.config(state="normal")

def next_question():
    global current_question
    current_question += 1

    if current_question < len(quiz):
        show_question()
    else:
        messagebox.showinfo("Quiz Completed", "You have completed the quiz!\nYour final score is: {}/{}".format(score, len(quiz)))
        root.destroy()

# Create main window
root = tk.Tk()
root.title("Quiz Game")
root.geometry("800x700")
style = Style(themename="flatly")
root.iconbitmap("C:\\Users\\theco\\OneDrive\\Desktop\\Coding things\\QuizApp\\iconquiz.ico")

# Create background
image_path = r"C:\Users\theco\OneDrive\Desktop\Coding things\QuizApp\tv.png"

original_image = Image.open(image_path)
resized_image = original_image.resize((900, 800), Image.Resampling.LANCZOS)

# Keep a reference so Tkinter does not remove the image
root.bg_photo = ImageTk.PhotoImage(resized_image)

bg_image = tk.Label(root, image=root.bg_photo)
bg_image.place(x=0, y=0, relwidth=1, relheight=1)
bg_image.lower()


# Configure the font size
style.configure("TLabel", font=("Courier New", 18, "bold"), background="#0A0A0A", foreground="white")
style.configure("TButton", font=("Courier New", 10, "bold"), background="#0A0A0A", foreground="white")

# Create the question label
question_label = ttk.Label(
    root,
    anchor="center",
    wraplength=500,
    padding=10
)
question_label.pack(pady=10)
question_label.place(x=150, y=600, width=500, height=80)

# Create choice buttons
choice_btns = []
for i in range(4):
    button = ttk.Button(
        root,
        command=lambda i=i: check_answer(i),
    )
    button.pack(pady=5)
    choice_btns.append(button)
    button.place(x=250, y=250 + i * 60, width=300, height=40)

# Crate feedback label
feedback_label = ttk.Label(
    root,
    anchor="center",
    padding=10
)
feedback_label.pack(pady=10)
feedback_label.place(x=5, y=350)

# Initialize the score
score = 0

# Create score label
score_label = ttk.Label(
    root,
    text="0/{}".format(len(quiz)),
    anchor="center",
    padding=10
)
score_label.pack(pady=10)
score_label.place(x=610, y=415)

# Create the next button
next_btn = ttk.Button(
    root,
    text="Next",
    command=next_question,
    state="disabled"
)
next_btn.pack(pady=10)
next_btn.place(x=610, y=500)

# Initialize the current question index
current_question = 0

# Show the first question
show_question()

# Start the main loop
root.mainloop()