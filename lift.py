from inc.image_classes import Image
import numpy as np

# A small value to avoid division by zero
EPSILON = 1e-6

image = Image("./images/checkout.png")

# Set the lift adjustment amount.
# A positive value brightens the shadows.
# A negative value darkens the shadows.
lift_amount = 0.2

# The lift adjustment formula is a linear addition to color values.
# It shifts the black point of the image.
for pixel in image.data():
    # We do not need to premultiply or unpremultiply here,
    # as lift is an in-place color operation.

    # Apply the lift formula to the red channel
    pixel.r = pixel.r + lift_amount

    # Apply the lift formula to the green channel
    pixel.g = pixel.g + lift_amount

    # Apply the lift formula to the blue channel
    pixel.b = pixel.b + lift_amount

    # Clamp the values to the valid 0-1 range to prevent overflow
    pixel.r = np.clip(pixel.r, 0, 1)
    pixel.g = np.clip(pixel.g, 0, 1)
    pixel.b = np.clip(pixel.b, 0, 1)

    # The alpha channel is not affected by color adjustments
    # and remains unchanged.

image.show(title=f"Lift corrected operation")
