from inc.image_classes import Image
import numpy as np

# A small value to avoid division by zero
EPSILON = 1e-6

image = Image("./images/checkout.png")

# Set the white point adjustment amount.
# A value > 1.0 brightens the highlights and increases contrast.
# A value < 1.0 darkens the highlights.
white_point = 1.2

# The white point adjustment formula is a linear multiplication
# that shifts the white point of the image.
for pixel in image.data():
    # We do not need to premultiply or unpremultiply here,
    # as this is an in-place color operation.

    # Apply the formula to the red channel
    pixel.r = pixel.r * white_point

    # Apply the formula to the green channel
    pixel.g = pixel.g * white_point

    # Apply the formula to the blue channel
    pixel.b = pixel.b * white_point

    # Clamp the values to the valid 0-1 range.
    # This is crucial for a white point adjustment, as it
    # ensures that values above the white point are clipped to 1 (white).
    pixel.r = np.clip(pixel.r, 0, 1)
    pixel.g = np.clip(pixel.g, 0, 1)
    pixel.b = np.clip(pixel.b, 0, 1)

    # The alpha channel is not affected by color adjustments
    # and remains unchanged.

image.show(title=f"White point adjusted by amount = {white_point}")
