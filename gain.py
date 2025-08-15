from inc.image_classes import Image
import numpy as np

# A small value to avoid division by zero
EPSILON = 1e-6

image = Image("./images/checkout.png")

# Set the gain adjustment factor.
# A value > 1.0 brightens the image.
# A value < 1.0 darkens the image.
gain_factor = 1.5

# The gain adjustment formula is a linear transformation: Final_Color = Color * gain_factor
for pixel in image.data():
    # We do not need to premultiply or unpremultiply here,
    # as gain is an in-place color operation.

    # Apply the gain formula to the red channel
    pixel.r = pixel.r * gain_factor

    # Apply the gain formula to the green channel
    pixel.g = pixel.g * gain_factor

    # Apply the gain formula to the blue channel
    pixel.b = pixel.b * gain_factor

    # Clamp the values to the valid 0-1 range to prevent overflow
    pixel.r = np.clip(pixel.r, 0, 1)
    pixel.g = np.clip(pixel.g, 0, 1)
    pixel.b = np.clip(pixel.b, 0, 1)

    # The alpha channel is not affected by color adjustments
    # and remains unchanged.

image.show(title=f"Gain adjusted by factor = {gain_factor}")
