from inc.image_classes import Image
import numpy as np

# A small value to avoid division by zero
EPSILON = 1e-6

image_one = Image("./images/checkout.png")

# Set the black point adjustment amount.
# A positive value makes shadows darker and increases contrast.
# A negative value brightens shadows.
black_point = 0.1

# The black point adjustment formula is a linear subtraction
# that shifts the black point of the image.
for pixel in image_one.data():
    # We do not need to premultiply or unpremultiply here,
    # as this is an in-place color operation.

    # Apply the formula to the red channel
    pixel.r = pixel.r - black_point

    # Apply the formula to the green channel
    pixel.g = pixel.g - black_point

    # Apply the formula to the blue channel
    pixel.b = pixel.b - black_point

    # Clamp the values to the valid 0-1 range.
    # This is crucial for a black point adjustment, as it
    # ensures that values below the black point are clipped to 0 (black).
    pixel.r = np.clip(pixel.r, 0, 1)
    pixel.g = np.clip(pixel.g, 0, 1)
    pixel.b = np.clip(pixel.b, 0, 1)

    # The alpha channel is not affected by color adjustments
    # and remains unchanged.

image_one.show(title=f"Black point adjusted operation")
