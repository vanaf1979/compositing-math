from inc.image_classes import Image
import numpy as np

# A small value to avoid division by zero
EPSILON = 1e-6

image = Image("./images/checkout.png")

# Set the gamma value.
# A value < 1.0 brightens the image.
# A value > 1.0 darkens the image.
gamma = 1.5

# The gamma correction formula is a non-linear transformation.
# It is calculated as Final_Color = Color^(1/gamma)
for pixel in image.data():
    # We do not need to premultiply or unpremultiply here,
    # as gamma correction is an in-place color operation.

    # Apply the gamma formula to the red channel
    pixel.r = np.power(pixel.r, 1 / gamma)

    # Apply the gamma formula to the green channel
    pixel.g = np.power(pixel.g, 1 / gamma)

    # Apply the gamma formula to the blue channel
    pixel.b = np.power(pixel.b, 1 / gamma)

    # Clamp the values to the valid 0-1 range to prevent overflow
    pixel.r = np.clip(pixel.r, 0, 1)
    pixel.g = np.clip(pixel.g, 0, 1)
    pixel.b = np.clip(pixel.b, 0, 1)

    # The alpha channel is not affected by color adjustments
    # and remains unchanged.

image.show(title=f"Gamma corrected operation")
