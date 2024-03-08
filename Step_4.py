from backend1 import encrypt_aes, hide_text_in_image, extract_text_from_image, decrypt_aes
import tkinter as tk
from tkinter import filedialog, messagebox

def encrypt_and_hide():
    message = message_entry.get()
    password = password_entry.get()
    image_path = image_path_var.get()

    if message and password and image_path:
        try:
            encrypted_message = encrypt_aes(message, password)
            hide_text_in_image(image_path, encrypted_message, "embedded_image.png")
            messagebox.showinfo("Success", "Steganography process completed successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    else:
        messagebox.showwarning("Warning", "Please enter a message, password, and choose an image.")


def decrypt_and_show():
    password = password_entry_decrypt.get()
    stego_image_path = stego_image_path_var.get()

    if password and stego_image_path:
        try:
            decrypted_message = extract_text_from_image(stego_image_path, password)
            decrypted_text_label.config(text="Decrypted message: " + decrypted_message, fg="green")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    else:
        messagebox.showwarning("Warning", "Please enter a password and choose an embedded image.")

def choose_image():
    file_path = filedialog.askopenfilename(title="Choose an Image File", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        image_path_var.set(file_path)
    else:
        image_path_var.set("No file chosen")

def choose_stego_image():
    file_path = filedialog.askopenfilename(title="Choose Embedded Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        stego_image_path_var.set(file_path)
    else:
        stego_image_path_var.set("No file chosen")

# Create the main window
window = tk.Tk()
window.title("Steganography with AES Encryption")
window.geometry("500x500")  # Set window size

# Add padding
padding_y = 10

# Create input fields and buttons for encryption
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

# Create input fields and buttons for decryption
password_label_decrypt = tk.Label(window, text="Enter the decryption password:", font=("Helvetica", 12))
password_label_decrypt.pack(pady=padding_y)
password_entry_decrypt = tk.Entry(window, width=30, show='*', font=("Helvetica", 12))
password_entry_decrypt.pack(pady=padding_y)

stego_image_label = tk.Label(window, text="Choose an embedded image for decryption:", font=("Helvetica", 12))
stego_image_label.pack(pady=padding_y)
stego_image_path_var = tk.StringVar()
stego_image_path_var.set("No file chosen")
stego_image_button = tk.Button(window, text="Choose Embedded Image", command=choose_stego_image, bg="orange", fg="white", font=("Helvetica", 12))
stego_image_button.pack(pady=padding_y)

decrypt_button = tk.Button(window, text="Decrypt and Show", command=decrypt_and_show, bg="green", fg="white", font=("Helvetica", 12))
decrypt_button.pack(pady=padding_y)

decrypted_text_label = tk.Label(window, text="", font=("Helvetica", 12))
decrypted_text_label.pack(pady=padding_y)

# Run the main loop
window.mainloop()
