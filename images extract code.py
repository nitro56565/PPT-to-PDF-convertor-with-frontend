import os
import fitz

def extract_images_from_pdf(file_path, output_dir):
    images = []
    try:
        with fitz.open(file_path) as pdf:
            for page_index, page in enumerate(pdf):
                image_list = page.get_images()
                for image_index, img in enumerate(image_list):
                    xref = img[0]
                    base_image = pdf.extract_image(xref)
                    image_data = base_image["image"]
                    image_ext = base_image["ext"]
                    image_name = f"image_page_{page_index + 1}_index_{image_index + 1}.{image_ext}"
                    image_path = os.path.join(output_dir, image_name)
                    with open(image_path, "wb") as f:
                        f.write(image_data)
                    images.append(image_path)
        return images
    except Exception as e:
        print(f"Error extracting images from PDF: {e}")
        return None

pdf_file_path = "E:/Games/sample2.pdf"
output_directory = "E:/Games/Images/"

# Extract images from PDF and save them to the output directory
image_paths = extract_images_from_pdf(pdf_file_path, output_directory)

if image_paths:
    # Process the extracted images as needed
    for image_path in image_paths:
        # Do something with each image
        print(f"Image path: {image_path}")