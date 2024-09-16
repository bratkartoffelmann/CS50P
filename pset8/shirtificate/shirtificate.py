from fpdf import FPDF
from PIL import Image, ImageDraw, ImageFont
import os

def main():
    name = input("Name: ").title().strip()
    shirt_output = f"shirtificate_{name}.png"

    create_shirt(name, shirt_output)
    create_shirt_pdf(shirt_output)
    
    # Remove shirt output
    os.remove(shirt_output)



def create_shirt(name, shirt_output):
    with Image.open("shirtificate.png") as im:
        draw = ImageDraw.Draw(im)

        # Define text and font
        text = f"{name} took CS50"
        font_size = 28
        # font = ImageFont.truetype("/Library/Fonts/Arial Bold.ttf", font_size)
        font = ImageFont.load_default() # Use this for submit50

        # Calculate text size and position
        text_bbox = draw.textbbox((0, 0), text, font=font)  # Bounding box of the text
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

        image_width, image_height = im.size
        text_x = (image_width - text_width) / 2
        text_y = (image_height - text_height) * 0.35

        # Define text color
        text_color = (255, 255, 255)  # White color

        # Draw text in the middle of the image
        draw.text((text_x, text_y), text, font=font, fill=text_color)

        # Save the modified image
        im.save(shirt_output)

def create_shirt_pdf(shirt_output):
    pdf = FPDF(orientation="P", format="A4")
    pdf.add_page()
    pdf.set_font('helvetica', 'B', 40) # Set font
    pdf.cell(0, 50, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align='C') # Show CS50 Shirtificate
    pdf.image(shirt_output, x='C', w=150) # Add Image
    pdf.output("shirtificate.pdf") # Save pdf

if __name__ == "__main__":
    main()