# Image-Background-Removal using rembg
This Python script utilizes the rembg library to remove backgrounds from images. It takes input images, removes the background, and saves the output images without the background.
# Dependencies
- python
- 'rembg' library
- 'numpy'
- 'PIL'(Python Imaging Library'
# Installation
1. Ensure you have Python 3.x installed on your system.
2. Install the required dependencies using pip:
-       pip install rembg numpy pillow
# Usage
1. Place the input images that you want to process in the same directory as the script or provide the full path to the input images.
2. Run the script by executing the following command in your terminal or command prompt:
-       python background_removal.py   
3. The script will process each input image, remove the background, and save the output images in the specified output directory.
# Input images
You can provide one or more input images to the script. Update the 'input_image_paths' list in the script to include the paths of the input images.
# Output images
The output images will be saved in the 'output_images' directory by default. You can change the output directory by modifying the 'output_directory' variable in the script.
# Example
Input images: 'dice1.jpg', 'dice2.jpg', 'dice3.jpg'
Output images will be saved as: 'output_dice1.jpg', 'output_dice2.jpg', 'output_dice3.jpg'
