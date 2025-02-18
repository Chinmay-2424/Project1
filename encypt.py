import cv2
import os
import string
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Hide the root Tkinter window
Tk().withdraw()

# Prompt the user to select an image file
image_path = askopenfilename(title="Select an image file", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])

if not image_path:
    print("No file selected.")
    exit()

img = cv2.imread(image_path)

if img is None:
    print("Error: Image not found or unable to load.")
    exit()

msg = input("Enter secret message:")
password = input("Enter a passcode:")

# Add a delimiter to the message
msg += "###"

d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

m = 0
n = 0
z = 0

for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n = n + 1
    m = n + 1
    z = (z + 1) % 3

encrypted_image_path = "encryptedImage.jpg"
cv2.imwrite(encrypted_image_path, img)
os.system(f"start {encrypted_image_path}")  # Use 'start' to open the image on Windows

# Save the password to a file for decryption
with open("password.txt", "w") as f:
    f.write(password)

print(f"Encrypted image saved at: {encrypted_image_path}")
