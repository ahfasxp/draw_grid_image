from PIL import Image, ImageDraw, ImageFont

def draw_grid(image_path, output_path, grid_size):
    # Open the image
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    # Get image dimensions
    width, height = image.size

    # Load a font
    font = ImageFont.load_default()

    # Function to convert column number to letter
    def column_to_letter(column):
        result = ""
        while column >= 0:
            result = chr(column % 26 + ord('A')) + result
            column = column // 26 - 1
        return result

    # Draw vertical and horizontal lines and coordinates
    for x in range(0, width, grid_size):
        for y in range(0, height, grid_size):
            draw.rectangle([(x, y), (x+grid_size, y+grid_size)], outline="red", width=1)
            column_letter = column_to_letter(x // grid_size)
            row_number = y // grid_size + 1
            coordinate = f"{column_letter}{row_number}"
            draw.text((x+5, y+5), coordinate, fill="red", font=font)

    # Konversi gambar ke mode RGB sebelum menyimpan
    if image.mode == 'RGBA':
        image = image.convert('RGB')

    # Simpan gambar output
    image.save(output_path)

# Contoh penggunaan
draw_grid("input_image.png", "output_image_with_grid.png", 300)
