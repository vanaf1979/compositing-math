from inc.image_classes import Image

image_in = Image("./images/checkout.png")

for pixel in image_in.data():

    # A basic desaturation averages the rbg values and stores it in all three channels.
    # This is optically incorrect. See desaturate_optically.py for a correct version.
    average = (pixel.r + pixel.g + pixel.b) / 3
    pixel.r = average
    pixel.g = average
    pixel.b = average


image_in.show(title="Screen Blend Mode")
