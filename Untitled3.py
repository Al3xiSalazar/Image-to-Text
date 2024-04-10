#!/usr/bin/env python
# coding: utf-8

# In[12]:


import cv2
import pytesseract
import PyPDF2
from PIL import Image
import tkinter as tk
from tkinter import filedialog
import pytesseract


# In[13]:


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    # Load image using OpenCV
    image = cv2.imread(image_path)
    
    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Use pytesseract to extract text from image
    extracted_text = pytesseract.image_to_string(gray_image)
    
    return extracted_text

# Example usage:
#if __name__ == "__main__":
    # Specify paths to image and PDF file
    #image_path = r""
    
    # Extract text from image
    #extracted_text_image = extract_text_from_image(image_path)
    #print("Extracted Text from Image:")
    #print(extracted_text_image)


# In[11]:


def extract_text_from_image(image_path):
    try:
        # Open the image file
        img = Image.open(image_path)
        # Perform OCR using Pytesseract
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        return str(e)

def browse_image():
    # Prompt user to select an image file
    file_path = filedialog.askopenfilename()
    if file_path:
        # Extract text from the selected image file
        extracted_text = extract_text_from_image(file_path)
        # Display the extracted text in a text box or console
        text_output.delete(1.0, tk.END)  # Clear previous text
        text_output.insert(tk.END, extracted_text)

# Create main application window
root = tk.Tk()
root.title("Image to Text Converter")

# Add button to browse for image file
browse_button = tk.Button(root, text="Select Image", command=browse_image)
browse_button.pack(pady=20)

# Add text box to display extracted text
text_output = tk.Text(root, height=10, width=50)
text_output.pack(pady=20)

# Start the GUI application loop
root.mainloop()


# In[ ]:




