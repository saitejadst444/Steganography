import cv2
import os
import string

def encrypt_image(image_path, msg, password):
    img = cv2.imread("puppy.jpg")  # Read the image

    # Create dictionaries for encryption and decryption
    d = {}
    c = {}
    for i in range(256):  # Update dictionary size to 256
        d[chr(i)] = i
        c[i] = chr(i)

    # Combine message and password into one string (password first)
    combined_msg = password + "|" + msg

    m = 0
    n = 0
    z = 0

    # Encrypt the combined message by modifying pixel values
    for i in range(len(combined_msg)):
        encrypted_value = d[combined_msg[i]] % 256  # Ensure value is within the 0-255 range
        img[n, m, z] = encrypted_value  # Replace pixel with message character's ASCII value
        n = n + 1
        m = m + 1
        z = (z + 1) % 3  # Loop through RGB channels

    # Save the encrypted image
    cv2.imwrite("encryptedImage.jpg", img)
    os.system("start encryptedImage.jpg")  # Open the image on Windows

    print("Image encrypted successfully.")

# Example usage:
message = input("Enter secret message: ")
password = input("Enter a passcode: ")
encrypt_image("mypic.jpg", message, password)
