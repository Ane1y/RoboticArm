from PIL import Image
import os


def compress_images(directory=False, quality=30):
    # 1. If there is a directory then change into it, else perform the next operations inside of the
    # current working directory:
    if directory:
        os.chdir(directory)

    # 2. Extract all of the .png and .jpeg files:
    files = os.listdir()

    # 3. Extract all of the images:
    images = [file for file in files if file.endswith(('jpg', 'png'))]

    # 4. Loop over every image:
    for image in images:
        print(image)

        # 5. Open every image:
        img = Image.open(image)

        # 5. Compress every image and save it with a new name:
        img.save("Compressed_and_resized_with_function_" + image, optimize=True, quality=quality)


subdirectory_path = 'C:\\Users\\vnkuk\\PycharmProjects\\pythonProject'
print(subdirectory_path)
compress_images(directory=subdirectory_path)