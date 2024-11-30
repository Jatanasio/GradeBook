import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

# Client setup
HOST = '127.0.0.1'  # Server IP address
PORT = 12345

class ChatClient:
    def __init__(self):
        # Create GUI
        self.window = tk.Tk()
        self.window.title("Chat App")
        
        # Chat display area
        self.chat_area = scrolledtext.ScrolledText(self.window, wrap=tk.WORD, state='disabled', height=20, width=50)
        self.chat_area.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        # Message entry field
        self.message_entry = tk.Entry(self.window, width=40)
        self.message_entry.grid(row=1, column=0, padx=10, pady=10)
        
        # Send button
        self.send_button = tk.Button(self.window, text="Send", width=10, command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=10, pady=10)
        
        # Quit button
        self.quit_button = tk.Button(self.window, text="Quit", width=10, command=self.quit_chat)
        self.quit_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        
        # Start client connection
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((HOST, PORT))
        
        # Thread to receive messages
        self.running = True
        self.username = None
        threading.Thread(target=self.receive_messages, daemon=True).start()
        
        self.prompt_username()

    def prompt_username(self):
        """Prompt for username before starting chat."""
        self.username_window = tk.Toplevel(self.window)
        self.username_window.title("Enter Username")
        
        tk.Label(self.username_window, text="Enter your username:").pack(pady=10)
        self.username_entry = tk.Entry(self.username_window, width=30)
        self.username_entry.pack(pady=5)
        tk.Button(self.username_window, text="Submit", command=self.submit_username).pack(pady=10)

    def submit_username(self):
        """Send username to the server."""
        self.username = self.username_entry.get().strip()
        if self.username:
            self.client.send(self.username.encode('utf-8'))
            self.username_window.destroy()

    def receive_messages(self):
        """Receive and display messages from the server."""
        while self.running:
            try:
                message = self.client.recv(1024).decode('utf-8')
                self.display_message(message)
            except:
                self.running = False
                self.client.close()
                break

    def display_message(self, message):
        """Display a message in the chat area."""
        self.chat_area.configure(state='normal')
        self.chat_area.insert(tk.END, message + '\n')
        self.chat_area.configure(state='disabled')
        self.chat_area.see(tk.END)

    def send_message(self):
        """Send a message to the server."""
        message = self.message_entry.get().strip()
        if message:
            if message.lower() == 'quit':
                self.quit_chat()
            else:
                self.client.send(message.encode('utf-8'))
                self.message_entry.delete(0, tk.END)

    def quit_chat(self):
        """Quit the chat gracefully."""
        self.running = False
        self.client.send("QUIT".encode('utf-8'))
        self.client.close()
        self.window.quit()

    def run(self):
        """Run the GUI."""
        self.window.mainloop()

if __name__ == "__main__":
    client = ChatClient()
    client.run()
