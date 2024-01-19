import spacy
import tkinter as tk
from tkinter import Scrollbar, Text, Entry, Button

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Function to get a response from the chatbot
def get_response(user_input):
    # Process the user input using spaCy
    doc = nlp(user_input)
    
    # Example rules for responses
    if "hi" in user_input.lower() or "hello" in user_input.lower():
        return "Hello! How can I help you today?"
    elif "how are you" in user_input.lower():
        return "I'm just a computer program, but thanks for asking!"
    elif "what is your name" in user_input.lower():
        return "I'm a simple chatbot. You can call me ChatGPT."
    elif "tell me a joke" in user_input.lower():
        return "Why don't scientists trust atoms? Because they make up everything!"
    elif "bye" in user_input.lower():
        return "Goodbye! If you have more questions, feel free to ask."
    else:
        return "I'm sorry, I didn't understand that. Can you please ask another question?"

# Function to handle user input and display responses in the GUI
def send_message():
    user_input = entry.get()
    response = get_response(user_input)
    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, f"You: {user_input}\nChatbot: {response}\n\n")
    chat_history.config(state=tk.DISABLED)
    entry.delete(0, tk.END)

# Main GUI window
root = tk.Tk()
root.title("Chatbot GUI")

# Chat history display
chat_history = Text(root, wrap=tk.WORD, state=tk.DISABLED)
chat_history.pack(expand=True, fill=tk.BOTH)

# Scrollbar for chat history
scrollbar = Scrollbar(root, command=chat_history.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chat_history.config(yscrollcommand=scrollbar.set)

# User input entry
entry = Entry(root, width=50)
entry.pack(pady=10)

# Send button
send_button = Button(root, text="Send", command=send_message)
send_button.pack()

# Run the GUI
root.mainloop()
