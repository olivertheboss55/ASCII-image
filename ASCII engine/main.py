from PIL import Image

# Load the image
image = Image.open("images/Mona_Lisa.jpg")

image = image.convert("L")  # Convert to grayscale

# Define the ASCII character set
ascii_characters = "`.-':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"

# Resize the image to desired dimensions
width, height = 100, 100
image = image.resize((width, height))

# Initialize the ASCII art text
ascii_art = ""

# Generate ASCII art
for y in range(height):
    for x in range(width):
        pixel_intensity = image.getpixel((x, y))
        ascii_character = ascii_characters[pixel_intensity * len(ascii_characters) // 256]
        ascii_art += ascii_character
    ascii_art += "\n"

# Display the ASCII art
print(ascii_art)
