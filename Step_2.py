import tkinter as tk
from tkinter import messagebox
from backend1 import encrypt_aes

def encrypt_message():
    message = message_entry.get()
    password = password_entry.get()

    if message and password:
        try:
            encrypted_message = encrypt_aes(message, password)
            result_label.config(text="Encrypted message: " + encrypted_message, fg="green")
        except Exception as e:
            messagebox.showerror("Error", "Encryption failed. Please try again.")
    else:
        result_label.config(text="Please enter a message and password.", fg="red")

# Create the main window
window = tk.Tk()
window.title("AES Encryption")
window.geometry("400x250")  # Set window size

# Add padding
padding_y = 10

# Create input fields and buttons
message_label = tk.Label(window, text="Enter your secret message:", font=("Helvetica", 12))
message_label.pack(pady=padding_y)
message_entry = tk.Entry(window, width=30, font=("Helvetica", 12))
message_entry.pack(pady=padding_y)

password_label = tk.Label(window, text="Enter a password for encryption:", font=("Helvetica", 12))
password_label.pack(pady=padding_y)
password_entry = tk.Entry(window, width=30, show='*', font=("Helvetica", 12))
password_entry.pack(pady=padding_y)

encrypt_button = tk.Button(window, text="Encrypt", command=encrypt_message, bg="blue", fg="white", font=("Helvetica", 12))
encrypt_button.pack(pady=padding_y)

result_label = tk.Label(window, text="", font=("Helvetica", 12))
result_label.pack(pady=padding_y)

# Run the main loop
window.mainloop()
