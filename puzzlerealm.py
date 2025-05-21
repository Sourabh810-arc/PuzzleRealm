import tkinter as tk
from tkinter import messagebox, simpledialog
import random
from PIL import Image, ImageTk
import os
import time

level_1_words = ['cat', 'dog', 'fish', 'bat', 'Chitkara', 'tab']
level_2_words = ['function', 'variable', 'array', 'object', 'string']
level_3_words = ['developer', 'algorithm', 'javascript', 'software', 'hardware']
level_4_words = ['abstraction', 'refactoring', 'encapsulation', 'inheritance', 'polymorphism']
level_5_words = ['metaprogramming', 'recursion', 'multithreading', 'microservices', 'concurrency']

level = 1
tries_left = 3
correct_word = ""

memory_level = 1
memory_sequence = []
user_sequence = []
memory_options = ['1', '2', '3', '4', 'Red', 'Blue', 'Green', 'Yellow', 'Apple', 'Dog', 'Python', 'Variable']

background_images = []
current_bg_image = None


general_knowledge_questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "Which planet is known as the Red Planet?", "answer": "Mars"},
    {"question": "What is the chemical symbol for water?", "answer": "H2O"},
    {"question": "Who painted the Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "What is the largest mammal in the world?", "answer": "Blue Whale"}
]

french_questions = [
    {"question": "Bonjour", "options": ["Hello", "Bye", "Thanks", "Thank you"], "answer": "Hello"},
    {"question": "Merci", "options": ["Please", "Sorry", "Thanks", "Hello"], "answer": "Thanks"},
    {"question": "Au revoir", "options": ["Goodbye", "Hello", "Thanks", "Yes"], "answer": "Goodbye"},
    {"question": "S'il vous plaît", "options": ["Sorry", "Please", "Yes", "No"], "answer": "Please"},
    {"question": "Pardon", "options": ["Hello", "Goodnight", "Excuse me", "Welcome"], "answer": "Excuse me"}
]

spanish_questions = [
    {"question": "Sí", "options": ["Hello", "Bye", "Yes", "Thank you"], "answer": "Yes"},
    {"question": "No", "options": ["Yes", "No", "Maybe", "Good"], "answer": "No"},
    {"question": "Gracias", "options": ["Thanks", "Hello", "Goodbye", "Sorry"], "answer": "Thanks"},
    {"question": "Hola", "options": ["Hello", "Bye", "Please", "Yes"], "answer": "Hello"},
    {"question": "Adiós", "options": ["Thanks", "Bye", "Excuse me", "Yes"], "answer": "Bye"}
]


def jumble_word(word):
    word = list(word)
    random.shuffle(word)
    return ''.join(word)

def load_background_images():
    global background_images
    image_paths = [
        "create a image of jumble word_   more impressive __ 29-03-2025 at 15-44-40.jpeg",
        "create a puzzle game image of jumble word_   more impressive __ 29-03-2025 at 15-41-01.jpeg",
        "create a puzzle game image of jumble word_   more impressive __ 29-03-2025 at 15-41-24.jpeg",
        "create a puzzle game image of memory game   more impressive __ 29-03-2025 at 15-40-06.jpeg"
    ]

    for path in image_paths:
        try:
            if os.path.exists(path):
                img = Image.open(path)
                img = img.resize((window.winfo_screenwidth(), window.winfo_screenheight()), Image.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                background_images.append(photo)
            else:
                img = Image.new('RGB', (window.winfo_screenwidth(), window.winfo_screenheight()),
                                color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
                background_images.append(ImageTk.PhotoImage(img))
        except:
            img = Image.new('RGB', (window.winfo_screenwidth(), window.winfo_screenheight()),
                            color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            background_images.append(ImageTk.PhotoImage(img))

def set_background_image():
    global current_bg_image
    if background_images:
        current_bg_image = random.choice(background_images)
        background_label.config(image=current_bg_image)
        background_label.image = current_bg_image

def start_game():
    global correct_word, tries_left, level
    window.title("PuzzleRealm - Jumbled Word Game")
    for widget in window.winfo_children():
        widget.pack_forget()

    game_frame.pack(expand=True)
    word_list = [level_1_words, level_2_words, level_3_words, level_4_words, level_5_words][level - 1]
    correct_word = random.choice(word_list)
    jumbled_word = jumble_word(correct_word)

    jumbled_word_label.config(text=f"Jumbled Word: {jumbled_word}")
    guess_entry.delete(0, tk.END)
    level_label.config(text=f"Level: {level}")
    tries_left = 3
    set_background_image()
    update_timer()

def check_guess():
    global tries_left, level
    guess = guess_entry.get().lower()

    if guess == correct_word:
        messagebox.showinfo("Correct!", f"Proceeding to level {level + 1}.")
        level += 1
        tries_left = 3
        set_background_image()
        if level > 5:
            game_frame.pack_forget()
            start_memory_game()
        else:
            start_game()
        show_learning_popup()  
    else:
        tries_left -= 1
        if tries_left > 0:
            messagebox.showerror("Incorrect", f"Try again! {tries_left} tries left.")
        else:
            jumbled_word_label.config(text=f"Jumbled Word: {jumble_word(correct_word)} ({correct_word})")
            show_custom_popup()

def show_custom_popup():
    popup = tk.Toplevel(window)
    popup.title("Game Over")
    popup.geometry("300x150")
    popup.configure(bg="#1A1A40")

    message = tk.Label(popup, text="Out of tries! Restart game?", font=("Arial", 12), bg="#1A1A40", fg="#FFD700")
    message.place(relx=0.5, rely=0.3, anchor="center")

    restart_button = tk.Button(popup, text="Yes", bg="#2196F3", fg="white", command=lambda: restart_game(popup))
    restart_button.place(relx=0.3, rely=0.7, anchor="center")

    quit_button = tk.Button(popup, text="No", bg="#F44336", fg="white", command=window.quit)
    quit_button.place(relx=0.7, rely=0.7, anchor="center")

def restart_game(popup):
    global level, tries_left
    level = 1
    tries_left = 3
    popup.destroy()
    start_game()

def show_learning_popup():
    popup = tk.Toplevel(window)
    popup.title("Quick Quiz")
    popup.geometry("280x180")
    popup.configure(bg="#333333")

    label = tk.Label(popup, text="Pick a quiz to continue:", font=("Arial", 12), bg="#333333", fg="white")
    label.pack(pady=10)

    lang_button = tk.Button(popup, text="Language Quiz", font=("Arial", 12), bg="#6A1B9A", fg="white", command=lambda: [popup.destroy(), choose_language_learning()])
    lang_button.pack(pady=5, padx=20, fill="x")

    gk_button = tk.Button(popup, text="General Knowledge", font=("Arial", 12), bg="#1E88E5", fg="white", command=lambda: [popup.destroy(), ask_general_knowledge()])
    gk_button.pack(pady=5, padx=20, fill="x")

def choose_language_learning():
    popup = tk.Toplevel(window)
    popup.title("Choose Language")
    popup.geometry("250x120")
    popup.configure(bg="#444444")

    french_button = tk.Button(popup, text="French", font=("Arial", 12), bg="#64B5F6", fg="white", command=lambda: [popup.destroy(), ask_french_question()])
    french_button.pack(pady=10, padx=20, fill="x")

    spanish_button = tk.Button(popup, text="Spanish", font=("Arial", 12), bg="#FFB300", fg="black", command=lambda: [popup.destroy(), ask_spanish_question()])
    spanish_button.pack(pady=10, padx=20, fill="x")

def ask_general_knowledge():
    question_data = random.choice(general_knowledge_questions)
    answer = simpledialog.askstring("General Knowledge", question_data['question'], parent=window)
    if answer is not None:
        if answer.lower() == question_data['answer'].lower():
            messagebox.showinfo("Correct!", "That's right!")
        else:
            messagebox.showerror("Incorrect", f"The correct answer was: {question_data['answer']}")

def ask_french_question():
    question_data = random.choice(french_questions)
    show_language_quiz("French Word Quiz", question_data)

def ask_spanish_question():
    question_data = random.choice(spanish_questions)
    show_language_quiz("Spanish Word Quiz", question_data)

def show_language_quiz(title, data):
    popup = tk.Toplevel(window)
    popup.title(title)
    popup.geometry("300x250")
    popup.configure(bg="#3E3E3E")

    q_label = tk.Label(popup, text=f"What does '{data['question']}' mean?", font=("Arial", 14), bg="#3E3E3E", fg="white")
    q_label.pack(pady=15)

    def check_choice(selected_option):
        if selected_option == data['answer']:
            messagebox.showinfo("Correct!", f"Yes, it means '{data['answer']}'.")
        else:
            messagebox.showerror("Incorrect", f"The correct answer is '{data['answer']}'.")
        popup.destroy()

    for opt in data['options']:
        btn = tk.Button(popup, text=opt, font=("Arial", 12), bg="#4CAF50", fg="white", command=lambda o=opt: check_choice(o))
        btn.pack(pady=5, padx=20, fill="x")

def start_memory_game():
    global memory_sequence, user_sequence, memory_level
    for widget in window.winfo_children():
        widget.pack_forget()

    window.title("PuzzleRealm - Memory Game")
    memory_frame.pack(expand=True)
    memory_title_label.config(text="Memory Game", font=("Helvetica", 18, 'bold'))
    memory_sequence = []
    user_sequence = []
    memory_level = 1

    memory_label.config(text="Watch carefully, remember the sequence!")
    memory_entry.delete(0, tk.END)
    set_background_image()
    generate_memory_sequence()
    update_timer()

def generate_memory_sequence():
    global memory_sequence, memory_level
    memory_sequence.append(random.choice(memory_options[:memory_level * 2]))
    display_sequence()

def display_sequence():
    delay = max(1000 - (memory_level - 1) * 150, 300)
    for i, item in enumerate(memory_sequence):
        window.after(i * delay, lambda n=item: memory_label.config(text=str(n)))
    window.after(len(memory_sequence) * delay + delay, lambda: memory_label.config(text="Enter the sequence:"))

def check_memory_input():
    global user_sequence, memory_level
    user_sequence = memory_entry.get().split()

    if user_sequence == memory_sequence:
        if memory_level < 5:
            memory_level += 1
            messagebox.showinfo("Success", f"Correct! Proceeding to level {memory_level}.")
            set_background_image()
            generate_memory_sequence()
            show_learning_popup()
        else:
            messagebox.showinfo("Congratulations!", "You completed all levels of the Memory Game!")
            show_learning_popup()
            window.quit()
    else:
        show_memory_game_popup()

def show_memory_game_popup():
    popup = tk.Toplevel(window)
    popup.title("Game Over")
    popup.geometry("300x150")
    popup.configure(bg="#1A1A40")

    message = tk.Label(popup, text="Wrong sequence! Play again?", font=("Arial", 12), bg="#1A1A40", fg="#FFD700")
    message.place(relx=0.5, rely=0.3, anchor="center")

    restart_button = tk.Button(popup, text="Yes", bg="#2196F3", fg="white", command=lambda: restart_memory_game(popup))
    restart_button.place(relx=0.3, rely=0.7, anchor="center")

    quit_button = tk.Button(popup, text="No", bg="#F44336", fg="white", command=window.quit)
    quit_button.place(relx=0.7, rely=0.7, anchor="center")

def restart_memory_game(popup):
    global memory_level, memory_sequence, user_sequence
    memory_level = 1
    memory_sequence = []
    user_sequence = []
    popup.destroy()
    start_memory_game()

window = tk.Tk()
window.title("PuzzleRealm")
window.geometry('500x600')
window.configure(bg='#2C003E')

background_label = tk.Label(window)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

load_background_images()
set_background_image()

title_label = tk.Label(window, text="Welcome to PuzzleRealm!", font=("Helvetica", 18, 'bold'), bg='#2C003E', fg='#FFD700')
title_label.pack(expand=True, pady=(10, 10))

start_button = tk.Button(window, text="Start Jumbled Word Game", font=("Arial", 14, 'bold'), bg='#4CAF50', fg='white', command=start_game)
start_button.pack(expand=True, pady=(10, 300))

game_frame = tk.Frame(window, bg="#2C003E")
level_label = tk.Label(game_frame, text="Level: 1", font=("Arial", 14), bg='#2C003E', fg='#FFD700')
jumbled_word_label = tk.Label(game_frame, text="Jumbled Word: ", font=("Arial", 16), bg='#2C003E', fg='#FFD700')
guess_entry = tk.Entry(game_frame, font=("Arial", 14), width=20, bd=3, relief="solid", justify='center')
submit_button = tk.Button(game_frame, text="Submit Guess", font=("Arial", 14, 'bold'), bg='#4CAF50', fg='white', command=check_guess)

level_label.pack(pady=5)
jumbled_word_label.pack(pady=15)
guess_entry.pack(pady=10)
submit_button.pack(pady=10)

memory_frame = tk.Frame(window, bg="#2C003E")
memory_title_label = tk.Label(memory_frame, text="", font=("Helvetica", 18, 'bold'), bg='#2C003E', fg='#FFD700')
memory_title_label.pack(pady=10)
memory_label = tk.Label(memory_frame, text="", font=("Arial", 18), bg='#2C003E', fg='#FFD700')
memory_entry = tk.Entry(memory_frame, font=("Arial", 14), width=30)
submit_memory_button = tk.Button(memory_frame, text="Submit", font=("Arial", 14), bg='#4CAF50', fg='white', command=check_memory_input)

memory_label.pack(pady=20)
memory_entry.pack(pady=10)
submit_memory_button.pack(pady=10)

start_time = time.time()
time_limit = 300

timer_label = tk.Label(window, font=("Arial", 12, 'bold'), bg="#2C003E", fg="white")
timer_label.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)

def update_timer():
    elapsed = time.time() - start_time
    remaining = max(0, int(time_limit - elapsed))
    mins, secs = divmod(remaining, 60)
    timer_label.config(text=f"⏳ {mins:02}:{secs:02}")
    if remaining <= 0:
        messagebox.showinfo("Time's up!", "You cannot play this game anymore since the time limit has been exceeded.")
        window.quit()
    else:
        window.after(1000, update_timer)

window.mainloop()