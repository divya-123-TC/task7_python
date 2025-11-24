from PIL import Image
import os

# FULL PATHS BASED ON YOUR SCREENSHOT
input_folder = r"C:\Users\Divya T C\OneDrive\python_internship\task7_image_resize\images"
output_folder = r"C:\Users\Divya T C\OneDrive\python_internship\task7_image_resize\output"

os.makedirs(output_folder, exist_ok=True)

new_size = (400, 400)

for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg", ".png", ".jpeg", ".webp")):
        img_path = os.path.join(input_folder, filename)
        
        img = Image.open(img_path)

        resized = img.resize(new_size)
        save_path = os.path.join(output_folder, filename)

        resized.save(save_path)

        print("Resized:", filename)

print("✔ All images resized successfully!")