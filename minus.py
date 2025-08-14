from inc.image_classes import Image
import numpy as np

image_one = Image("./images/face.png")
image_two = Image("./images/checkout.png")

for background, foreground in zip(image_one.data(), image_two.data()):
    # Un-premultiply the color channels to work with straight values from each image before blending
    # Not needed in this example because the data is not multiplied yet.
    # background.unpremultiply()
    # foreground.unpremultiply()

    # The correct Minus calculation is applied to the straight color values.
    # The formula is: Background - Foreground
    background.r = background.r - foreground.r
    background.g = background.g - foreground.g
    background.b = background.b - foreground.b

    # Clamp the values to the valid 0-1 range. This is essential for
    # the Minus operation, as the result can be negative.
    background.r = np.clip(background.r, 0, 1)
    background.g = np.clip(background.g, 0, 1)
    background.b = np.clip(background.b, 0, 1)

    # The correct 'over' operation for the alpha channel
    # Applies the formula: Fg.a + Bg.a * (1 - Fg.a)
    background.a = foreground.a + background.a * (1 - foreground.a)

    # Re-premultiply the final blended pixel
    background.premultiply()

image_one.show(title="Minus operation")
