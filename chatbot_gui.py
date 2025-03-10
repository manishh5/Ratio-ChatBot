import tkinter as tk
import pandas as pd
from responses import ChatBot

class ChatGUI:
    def __init__(self, chatbot):
        self.chatbot = chatbot
        self.window = tk.Tk()
        self.window.title("Ratio ChatBot")

        self.response_text = tk.Text(self.window,height=30, width=40,background="lavender")
        self.response_text.pack()
        
        self.send_button = tk.Button(self.window, text="  Send  ", command=self.send_message,background="lavender",foreground="black")
        self.send_button.pack()
        
        self.text_entry = tk.Text(self.window, height=2, width=35, font=("cambria"),background="lavender")
        self.text_entry.pack()

    def send_message(self):
        message = self.text_entry.get("1.0", tk.END)
        self.response_text.insert(tk.END, f"You:  {message}\n","right")
        self.response_text.tag_config("right", justify=tk.RIGHT, lmargin1=200,font=("cambria"))
        response = self.chatbot.respond(message)
        self.response_text.insert(tk.END, f"Ratio:  {response}\n","font")
        self.response_text.tag_config("font",font=("cambria"))
        self.text_entry.delete("1.0", tk.END)
        
         
    def run(self):
        self.window.mainloop()

def main():
    chatbot = ChatBot("Ratio")
    gui = ChatGUI(chatbot)
    gui.run()

if __name__ == "__main__":
    main()