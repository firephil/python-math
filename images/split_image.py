from PIL import Image
import os


# use parcify.py instead of manual spliting


# Get the current directory
dir = os.path.dirname(__file__)

# Check image dimensions
image_path = os.path.join(dir, "sample.png")
image = Image.open(image_path)
image_width, image_height = image.size

# Adjust cropping coordinates based on image dimensions
if (image_width % 3 != 0):
    raise ValueError(
        "Image width is not divisible by 3. Cannot split image into 3 equal pieces."
    )

if (image_height % 3 != 0):
    raise ValueError(
        "Image height is not divisible by 3. Cannot split image into 3 equal pieces."
    )

# Split the image into 3 equal pieces
x_increment = image_width // 6
y_increment = image_height // 6
images = []
for i in range(6):
    piece_width = x_increment if i < 2 else image_width
    piece_height = y_increment if i < 2 else image_height
    piece = image.crop((i * x_increment, i * y_increment, (i + 1) * x_increment, (i + 1) * y_increment))
    images.append(piece)

# Save the individual pieces
for i, image in enumerate(images):
    image.save(os.path.join(dir,f'piece_{i:03d}.png'))