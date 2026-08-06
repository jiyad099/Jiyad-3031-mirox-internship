from PIL import Image, ImageFilter


def strip_exif(img):

    clean_image = Image.new(img.mode, img.size)

    clean_image.putdata(list(img.getdata()))

    return clean_image


def smooth_pixels(img):

    blurred = img.filter(ImageFilter.GaussianBlur(radius=2))

    return blurred


if __name__ == "__main__":

    image = Image.open("clean_photo.jpg")

    image = strip_exif(image)

    image = smooth_pixels(image)

    image.save("defended_image.jpg")

    print("Defended image saved successfully.")