from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes,padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from PIL import Image
import os
import base64

def encrypt(message, password):
    # Simple encryption using base64 encoding
    encoded_message = base64.b64encode(message.encode()).decode()
    encrypted_message = f"{password}_{encoded_message}"
    return encrypted_message

def derive_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        salt=salt,
        iterations=100000,
        length=32,  # Length of the derived key in bytes
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def encrypt_aes(message, password):
    salt = os.urandom(16)
    key = derive_key(password, salt)
    cipher = Cipher(algorithms.AES(key), modes.CFB8(salt), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(message.encode()) + encryptor.finalize()
    encrypted_message = base64.urlsafe_b64encode(salt + ciphertext).decode()
    return encrypted_message

def hide_text_in_image(image_path, encrypted_message, output_path):
    image = Image.open(image_path)
    pixels = list(image.getdata())
    binary_message = ''.join(format(ord(char), '08b') for char in encrypted_message)
    binary_message += '1111111111111110'  # Adding a delimiter to mark the end of the message

    index = 0
    for pixel in pixels:
        new_pixel = list(pixel)
        for i in range(3):  # Iterate over RGB components
            if index < len(binary_message):
                new_pixel[i] = int(bin(pixel[i])[2:-1] + binary_message[index], 2)
                index += 1
        pixels[pixels.index(pixel)] = tuple(new_pixel)

    stego_image = Image.new('RGB', image.size)
    stego_image.putdata(pixels)
    stego_image.save(output_path)
# Assume that the derive_key function is defined as before

def extract_text_from_image(image_path, password):
    image = Image.open(image_path)
    pixels = list(image.getdata())

    binary_message = ''
    for pixel in pixels:
        for i in range(3):  # Iterate over RGB components
            binary_message += bin(pixel[i])[-1]

    delimiter_index = binary_message.find('1111111111111110')
    binary_message = binary_message[:delimiter_index]

    decrypted_message = ''
    for i in range(0, len(binary_message), 8):
        decrypted_message += chr(int(binary_message[i:i+8], 2))

    base64_encoded_message = base64.b64encode(decrypted_message.encode()).decode()
    return base64_encoded_message
# def extract_text_from_image(image_path, password):
#     image = Image.open(image_path)
#     pixels = list(image.getdata())

#     binary_message = ''
#     for pixel in pixels:
#         for i in range(3):  # Iterate over RGB components
#             binary_message += bin(pixel[i])[-1]

#     delimiter_index = binary_message.find('1111111111111110')
#     binary_message = binary_message[:delimiter_index]

#     decrypted_message = ''
#     for i in range(0, len(binary_message), 8):
#         decrypted_message += chr(int(binary_message[i:i+8], 2))

#     decrypted_message = decrypt_aes(decrypted_message, password)
#     return decrypted_message

def decrypt_aes(encrypted_message, password):
    decoded_message = base64.urlsafe_b64decode(encrypted_message.encode())
    salt = decoded_message[:16]
    key = derive_key(password, salt)
    cipher = Cipher(algorithms.AES(key), modes.CFB8(salt), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_message = decryptor.update(decoded_message[16:]) + decryptor.finalize()
    return decrypted_message.decode()



