# utils.py
from rembg import remove
from PIL import Image
import matplotlib.pyplot as plt

def process_image(input_path, output_path):
    try:
        inp = Image.open(input_path)
        output = remove(inp)
        output.save(output_path)
        print(f"Image saved successfully at {output_path}")
    except Exception as e:
        print(f"Error processing the image: {e}")

def display_image(output_path):
    try:
        img = Image.open(output_path)
        plt.imshow(img)
        plt.axis('off')  # Hide axes for a cleaner look
        plt.show()
    except Exception as e:
        print(f"Error displaying the image: {e}")
