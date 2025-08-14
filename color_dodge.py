from inc.image_classes import Image
import numpy as np

EPSILON = 1e-6

image_one = Image("./images/face.png")
image_two = Image("./images/checkout.png")

for background, foreground in zip(image_one.data(), image_two.data()):
    # Un-premultiply the color channels to work with straight values from each image before blending
    # Not needed in this example because the data is not multiplied yet.
    # background.unpremultiply()
    # foreground.unpremultiply()

    # The correct Color Dodge calculation is applied to the straight color values.
    # The formula is: Bg / (1 - Fg)
    background.r = background.r / (1 - foreground.r + EPSILON) if foreground.r < 1 else 1.0
    background.g = background.g / (1 - foreground.g + EPSILON) if foreground.g < 1 else 1.0
    background.b = background.b / (1 - foreground.b + EPSILON) if foreground.b < 1 else 1.0

    # Clamp the values to the valid 0-1 range to prevent overflow
    background.r = np.clip(background.r, 0, 1)
    background.g = np.clip(background.g, 0, 1)
    background.b = np.clip(background.b, 0, 1)

    # The correct 'over' operation for the alpha channel
    # Applies the formula: Fg.a + Bg.a * (1 - Fg.a)
    background.a = foreground.a + background.a * (1 - foreground.a)

    # Re-premultiply the final blended pixel
    background.premultiply()

image_one.show(title="Color dodge operation")
