from PIL import Image

def crop_image(image_path, left, top, right, bottom, output_path="cropped_image.png"):
  """
  Crops an image based on given coordinates.

  Args:
    image_path: Path to the image file.
    left: X-coordinate of the left edge of the cropping box.
    top: Y-coordinate of the top edge of the cropping box.
    right: X-coordinate of the right edge of the cropping box.
    bottom: Y-coordinate of the bottom edge of the cropping box.
    output_path: Path to the output file of the cropped image (default: "cropped_image.png").

  Returns:
    None, but saves the cropped image to the output file.
  """

  # Open the image
  img = Image.open(image_path)

  # Crop the image
  cropped_img = img.crop((left, top, right, bottom))

  # Save the cropped image
  cropped_img.save(output_path)

# Example usage:
crop_image("grid_image.png", 1500, 600, 2100, 900)