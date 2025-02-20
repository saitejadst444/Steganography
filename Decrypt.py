import cv2

def decrypt_image(encrypted_image_path, user_password):
    img = cv2.imread("encryptedImage.jpg")  
    c = {}
    for i in range(256):  
        c[i] = chr(i)
    extracted_password = ""
    extracted_message = ""
    n = 0
    m = 0
    z = 0
    while True:
        if n >= img.shape[0] or m >= img.shape[1]: 
            break
        char = c[img[n, m, z] % 256]  
        if char == "|":  
            break
        extracted_password += char
        n = n + 1
        m = m + 1
        z = (z + 1) % 3

    while n < img.shape[0] and m < img.shape[1]:
        extracted_message += c[img[n, m, z] % 256]  
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    if extracted_password == user_password:
        print("Password is correct. Decrypted message:", extracted_message)
    else:
        print("Incorrect password. Decryption failed!")

user_password = input("Enter passcode for Decryption: ")
decrypt_image("encryptedImage.jpg", user_password)
