from inc.image_classes import Image
import numpy as np

# A small value to avoid division by zero
EPSILON = 1e-6

image = Image("./images/checkout.png")

# Set the contrast adjustment factor.
# A value > 1 increases contrast. A value < 1 decreases it.
contrast_factor = 1.5

for pixel in image.data():
    # The contrast adjustment formula is a linear transformation.
    # We pivot around 0.5 (middle gray) to darken shadows and brighten highlights.

    # We do not need to premultiply or unpremultiply here,
    # as contrast is an in-place color operation.

    # Apply the formula to the red channel
    pixel.r = (pixel.r - 0.5) * contrast_factor + 0.5

    # Apply the formula to the green channel
    pixel.g = (pixel.g - 0.5) * contrast_factor + 0.5

    # Apply the formula to the blue channel
    pixel.b = (pixel.b - 0.5) * contrast_factor + 0.5

    # Clamp the values to the valid 0-1 range to prevent overflow
    pixel.r = np.clip(pixel.r, 0, 1)
    pixel.g = np.clip(pixel.g, 0, 1)
    pixel.b = np.clip(pixel.b, 0, 1)

    # The alpha channel is not affected by color adjustments
    # and remains unchanged.

image.show(title=f"Contrast adjustment operation")
