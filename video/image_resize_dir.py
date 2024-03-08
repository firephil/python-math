from PIL import Image
import os

dim = (640,360)
output_directory = "out"
input = "images"
os.makedirs(output_directory, exist_ok=True)

for filename in os.listdir(input):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Open the image
        image_path = os.path.join(input, filename)
        img = Image.open(image_path)
        img = img.resize(dim)
        output_path = os.path.join(output_directory, filename)
        img.save(output_path)