import tkinter as tk
from tkinter import filedialog, messagebox
from backend1 import encrypt_aes, hide_text_in_image

def encrypt_and_hide():
    message = message_entry.get()
    password = password_entry.get()
    image_path = image_path_var.get()

    if message and password and image_path:
        try:
            encrypted_message = encrypt_aes(message, password)
            hide_text_in_image(image_path, encrypted_message, "embeded_image.png")
            messagebox.showinfo("Success", "Steganography process completed successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    else:
        messagebox.showwarning("Warning", "Please enter a message, password, and choose an image.")

def choose_image():
    file_path = filedialog.askopenfilename(title="Choose an Image File", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        image_path_var.set(file_path)
    else:
        image_path_var.set("No file chosen")

# Create the main window
window = tk.Tk()
window.title("Steganography with AES Encryption")
window.geometry("500x300")  # Set window size

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

image_label = tk.Label(window, text="Choose an image for steganography:", font=("Helvetica", 12))
image_label.pack(pady=padding_y)
image_path_var = tk.StringVar()
image_path_var.set("No file chosen")
image_button = tk.Button(window, text="Choose Image", command=choose_image, bg="green", fg="white", font=("Helvetica", 12))
image_button.pack(pady=padding_y)

encrypt_button = tk.Button(window, text="Encrypt and Hide", command=encrypt_and_hide, bg="blue", fg="white", font=("Helvetica", 12))
encrypt_button.pack(pady=padding_y)

# Run the main loop
window.mainloop()
