# main.py
from utils import process_image, display_image

def main():
    input_path = input("Enter the path to the input image (e.g., 'clgot.jpeg'): ")
    output_path = input("Enter the path to save the output image (e.g., 'clgot.png'): ")

    # Process the image
    process_image(input_path, output_path)

    # Display the result
    display_image(output_path)

if __name__ == "__main__":
    main()
