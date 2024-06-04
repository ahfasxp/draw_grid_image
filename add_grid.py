from PIL import Image, ImageDraw, ImageFont

def draw_grid(image_path, output_path, grid_size):
    # Open the image (background)
    background = Image.open(image_path)
    width, height = background.size

    # Create a new image with transparent background
    image = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)

    # Load a font
    font = ImageFont.truetype("arial.ttf", 50)  # Specify a font and size

    # Function to convert column number to letter
    def column_to_letter(column):
        result = ""
        while column >= 0:
            result = chr(column % 26 + ord('A')) + result
            column = column // 26 - 1
        return result

    # Opacity value
    opacity = 20

    # Define colors with reduced opacity
    colors = [
        (255, 0, 0, opacity),    # Red with transparency
        (0, 255, 0, opacity),    # Green with transparency
        (0, 0, 255, opacity),    # Blue with transparency
        (255, 255, 0, opacity),  # Yellow with transparency
        (255, 0, 255, opacity),  # Magenta with transparency
        (0, 255, 255, opacity)   # Cyan with transparency
    ]

    # Draw vertical and horizontal lines and coordinates
    for x in range(0, width, grid_size):
        for y in range(0, height, grid_size):
            # Determine color based on overall position
            color_index = (x // grid_size) + (y // grid_size * (width // grid_size))
            color = colors[color_index % len(colors)]
            draw.rectangle([(x, y), (x+grid_size, y+grid_size)], outline=None, fill=color)
            column_letter = column_to_letter(x // grid_size)
            row_number = y // grid_size + 1
            coordinate = f"{column_letter}{row_number}"
            # Calculate text position to be centered within the grid cell
            mask = font.getmask(coordinate) # Get the mask of the text
            text_width = mask.size[0]
            text_height = mask.size[1]
            text_x = x + (grid_size - text_width) // 2
            text_y = y + (grid_size - text_height) // 2
            draw.text((text_x, text_y), coordinate, fill="red", font=font)

    # Combine the background image with the grid image
    combined = Image.alpha_composite(background.convert("RGBA"), image)

    # Save the output image
    combined.save(output_path)

# Example usage
draw_grid("input_image.png", "output_image_with_grid.png", 300)