from PIL import Image

def load_image(file_path):
    return Image.open(file_path).convert("RGB")

def compare_images(file_path1, file_path2):
    img1 = load_image(file_path1)
    img2 = load_image(file_path2)

    if img1.size != img2.size:
        raise ValueError("Images must have the same dimensions.")

    diff_sum = 0
    for x in range(img1.width):
        for y in range(img1.height):
            pixel1 = img1.getpixel((x, y))
            pixel2 = img2.getpixel((x, y))

            diff_sum += sum([abs(c1 - c2) for c1, c2 in zip(pixel1, pixel2)])

    img_diff_percent = (diff_sum / (3 * img1.width * img1.height)) * 100
    return img_diff_percent

file_path1 = "path/to/image1.jpg"
file_path2 = "path/to/image2.jpg"

diff_percent = compare_images(file_path1, file_path2)
print(f"The difference between the two images is {diff_percent}%")
