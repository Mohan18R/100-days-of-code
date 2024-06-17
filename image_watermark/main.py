import tkinter as tk
from tkinter import filedialog,messagebox
from PIL import Image,ImageDraw,ImageFont


# Function to open a file dialog and get the image file path
def open_image():
    filepath=filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if filepath:
        add_watermark(filepath)

#Function to add watermark to the image
def add_watermark(filepath):
    try:
        image=Image.open(filepath)

        # Resize image if larger than 600x600
        max_size = (600, 600)
        image.thumbnail(max_size)

        # Create a transparent layer for the watermark
        watermark = Image.new("RGBA", image.size, (255, 255, 255, 0))

        # Load a font
        font = ImageFont.load_default()

        # Draw watermark (text or logo)
        draw = ImageDraw.Draw(watermark)
        text = "watermark"
        draw.text((10, 10), text, font=font, fill=(255, 255, 255, 128))

        # Combine the image with the watermark
        watermarked_image = Image.alpha_composite(image.convert("RGBA"), watermark)

        # Save or display the watermarked image
        watermarked_image.show()
        # watermarked_image.save("output.png")  # Save the watermarked image

    except Exception as e:
        messagebox.showerror("Error", f"Error adding watermark: {str(e)}")

# Create the main application window
root = tk.Tk()
root.title("Image Watermark App")

# Set the size of the window
root.geometry("300x300")
# Create and position the Upload button
upload_button = tk.Button(root, text="Upload Image", command=open_image, bg="#4CAF50", fg="white", font=("Helvetica", 16, "bold"), padx=20, pady=10)
upload_button.pack(pady=50)
# Run the Tkinter event loop
root.mainloop()

