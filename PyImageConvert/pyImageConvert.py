from PIL import Image
import os

input = open("C:\ConfigTool\image_convert_config.txt","r")
def resize_and_compress_image(input_path, output_path, target_width, target_height, target_size_kb):
    with Image.open(input_path) as img:
        img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
        quality = 85
        while True:
            img.save(output_path, optimize=True, quality=quality)
            if os.path.getsize(output_path) <= target_size_kb * 1024 or quality <= 5:
                break
            quality -= 5

def process_images(input_dir, output_dir, target_width, target_height, target_size_kb):
    os.makedirs(output_dir, exist_ok=True)
    
    for filename in os.listdir(input_dir):
        if filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg') or filename.lower().endswith('.png'):
            print("Converting: "+ filename)
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            resize_and_compress_image(input_path, output_path, target_width, target_height, target_size_kb)

input_directory = input.readline().split("=")[1].strip()
output_directory = input.readline().split("=")[1].strip()
target_width = int(input.readline().split("=")[1].strip())
target_height = int(input.readline().split("=")[1].strip())
target_size_kb = int(input.readline().split("=")[1].strip())

process_images(input_directory, output_directory, target_width, target_height, target_size_kb)
