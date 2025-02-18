import cv2
import os
import string
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Hide the root Tkinter window
Tk().withdraw()

# Prompt the user to select an encrypted image file
image_path = askopenfilename(title="Select an encrypted image file", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])

if not image_path:
    print("No file selected.")
    exit()

img = cv2.imread(image_path)

if img is None:
    print("Error: Image not found or unable to load.")
    exit()

# Load the password from the file
with open("password.txt", "r") as f:
    password = f.read()

pas = input("Enter passcode for Decryption:")

d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

message = ""
n = 0
m = 0
z = 0

if password == pas:
    while True:
        try:
            pixel_value = img[n, m, z]
            if pixel_value in c:
                char = c[pixel_value]
                if message.endswith("###"):
                    message = message[:-3]  # Remove the delimiter
                    break
                message += char
            n += 1
            m += 1
            z = (z + 1) % 3
        except IndexError:
            break
    print("Decryption message:", message)
else:
    print("YOU ARE NOT auth")
