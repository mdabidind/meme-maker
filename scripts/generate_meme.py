import sys
from PIL import Image, ImageDraw, ImageFont
import os

def draw_text_center(draw, text, font, y_pos, image_width):
    text_width, text_height = draw.textsize(text, font=font)
    x = (image_width - text_width) / 2
    draw.text((x, y_pos), text, font=font, fill='white', stroke_width=2, stroke_fill='black')

def generate_meme(input_path, top_text, bottom_text, output_path):
    try:
        img = Image.open(input_path).convert("RGB")
    except FileNotFoundError:
        print(f"Image not found: {input_path}")
        return

    width, height = img.size
    draw = ImageDraw.Draw(img)

    # Try to use Impact font, fallback to DejaVuSans
    try:
        font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
        font = ImageFont.truetype(font_path, size=int(height / 10))
    except:
        font = ImageFont.load_default()

    # Draw top and bottom text
    if top_text:
        draw_text_center(draw, top_text.upper(), font, 10, width)

    if bottom_text:
        draw_text_center(draw, bottom_text.upper(), font, height - int(height / 8), width)

    img.save(output_path)
    print(f"Meme saved to {output_path}")

if __name__ == "__main__":
    if len(sys.ar

