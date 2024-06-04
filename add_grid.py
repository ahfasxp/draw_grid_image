from PIL import Image, ImageDraw, ImageFont

def draw_grid(image_path, output_path, grid_size):
    # Open the image
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    # Get image dimensions
    width, height = image.size

    # Load a font
    font = ImageFont.load_default()

    # Draw vertical and horizontal lines
    for x in range(0, width, grid_size):
        for y in range(0, height, grid_size):
            draw.rectangle([(x, y), (x+grid_size, y+grid_size)], outline="red", width=1)
            draw.text((x+5, y+5), f"{x//grid_size},{y//grid_size}", fill="red", font=font)

    # Konversi gambar ke mode RGB sebelum menyimpan
    if image.mode == 'RGBA':
        image = image.convert('RGB')

    # Simpan gambar output
    image.save(output_path)

# Contoh penggunaan
draw_grid("input_image.png", "output_image_with_grid.png", 300)
