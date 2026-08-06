from PIL import Image
import numpy as np
import piexif
import os


# ---------- Helper Function ----------
def text_to_binary(text):
    binary = ""

    for char in text:
        binary += format(ord(char), "08b")

    return binary


# ---------- EXIF Injection ----------
def inject_exif(image, prompt):


    exif_dict = {
        "0th": {},
        "Exif": {},
        "GPS": {},
        "Interop": {},
        "1st": {},
        "thumbnail": None
    }

    exif_dict["0th"][piexif.ImageIFD.ImageDescription] = prompt

    exif_bytes = piexif.dump(exif_dict)

    image.info["exif"] = exif_bytes

    return image


# ---------- LSB Injection ----------
def inject_lsb(image, prompt):

    image = image.convert("RGB")

    binary_message = text_to_binary(prompt)

    width, height = image.size

    capacity = width * height

    if len(binary_message) > capacity:
        raise ValueError("Message is too large for this image.")

    index = 0

    for y in range(height):

        for x in range(width):

            if index >= len(binary_message):
                break

            r, g, b = image.getpixel((x, y))

            bit = int(binary_message[index])

            # Replace the least significant bit of the Red channel
            r = (r & 254) | bit

            image.putpixel((x, y), (r, g, b))

            index += 1

        if index >= len(binary_message):
            break

    return image