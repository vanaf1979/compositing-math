from inc.image_classes import Image

image_in = Image("./images/checkout.png")

for pixel in image_in.data():

    # The optically correct way to do desaturation based on the Rec 709 standard.
    # https://en.wikipedia.org/wiki/Rec._709

    # Convert channels to Rec 709 standard.
    r = pixel.r * 0.2126
    g = pixel.g * 0.7152
    b = pixel.b * 0.0722

    # Sum all the channels
    sum = r + g + b

    # Push the sum to all the channels
    # pixel.r = sum
    # pixel.g = sum
    # pixel.b = sum

    # Optional
    # We can set a factor by which the image has to be desaturated.
    # 0 = No desaturation
    # 1 = Full desaturation
    factor = 0.5

    pixel.r = pixel.r + factor * (sum - pixel.r)
    pixel.g = pixel.g + factor * (sum - pixel.g)
    pixel.b = pixel.b + factor * (sum - pixel.b)


image_in.show(title="Screen Blend Mode")
