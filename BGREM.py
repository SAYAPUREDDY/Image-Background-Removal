import rembg
import numpy as np
from PIL import Image
import os

def remove_background(input_path, output_path):
    try:
        input_image = Image.open(input_path)
        input_array = np.array(input_image)

        # Apply background removal using rembg
        output_array = rembg.remove(input_array)

        # Create a PIL Image from the output array
        output_image = Image.fromarray(output_array)

        # Convert the image to RGB mode (remove alpha channel)
        output_image = output_image.convert("RGB")

        # Save the output image as JPEG
        output_image.save(output_path, "JPEG")

        print(f"Background removed successfully. Output saved to {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

def remove_background_batch(input_paths, output_dir):
    for input_path in input_paths:
        # Generate output path based on the input filename
        input_filename = input_path.split("/")[-1]
        output_path = f"{output_dir}/output_{input_filename}"

        # Call the remove_background function for each input image
        remove_background(input_path, output_path)

if __name__ == "__main__":
    input_image_paths = ["C:/Users/91965/dice1.jpg", "C:/Users/91965/dice2.jpg", "C:/Users/91965/dice3.jpg"]
    output_directory = "output_images"

    # Create output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Call remove_background_batch to process multiple images
    remove_background_batch(input_image_paths, output_directory)
