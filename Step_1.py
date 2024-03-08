import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from functools import partial
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

def choose_image():
    file_path = filedialog.askopenfilename(title="Choose an Image File", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        image_path_var.set(file_path)
    else:
        image_path_var.set("No file chosen")

# Create the main window
window = tk.Tk()
window.title("Message Encryption")
window.geometry("500x300")  # Set window size

# Add padding
padding_x = 10
padding_y = 5

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

image_label = tk.Label(window, text="Choose an image for encryption:", font=("Helvetica", 12))
image_label.pack(pady=padding_y)
image_path_var = tk.StringVar()
image_path_var.set("No file chosen")
image_button = tk.Button(window, text="Choose Image", command=choose_image, bg="orange", fg="white", font=("Helvetica", 12))
image_button.pack(pady=padding_y)

result_label = tk.Label(window, text="", font=("Helvetica", 12))
result_label.pack(pady=padding_y)

# Run the main loop
window.mainloop()
