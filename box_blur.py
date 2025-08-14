import cv2
import numpy as np

# Load the image
# You can replace 'your_image.jpg' with the path to your image
image = cv2.imread('./images/checkout.png')

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load image.")
else:
    # Get the dimensions of the image
    height, width, channels = image.shape

    # Define the kernel size for the blur
    kernel_size = 15

    # Create an output image array with the same dimensions as the original, initialized to zeros
    # This will be where the blurred pixels are stored
    blurred_image = np.zeros_like(image)

    # Calculate the padding needed to handle the edges of the image
    # This ensures the kernel doesn't go out of bounds
    pad_size = kernel_size // 2

    # Iterate through each pixel of the image, excluding the padded edges
    # 'y' represents the row (height) and 'x' represents the column (width)
    for y in range(pad_size, height - pad_size):
        for x in range(pad_size, width - pad_size):
            # For each pixel (x, y), extract the region of interest (ROI)
            # This ROI is the area of the image covered by the kernel
            # It's a slice of the image from (y - pad_size) to (y + pad_size + 1)
            # and from (x - pad_size) to (x + pad_size + 1)
            roi = image[y - pad_size : y + pad_size + 1, x - pad_size : x + pad_size + 1]

            # Calculate the average of all pixel values within the ROI
            # `np.mean()` calculates the arithmetic mean along the specified axes
            # For a box blur, the average is taken across all pixels in the ROI
            average_color = np.mean(roi, axis=(0, 1))

            # Assign the calculated average color to the corresponding pixel in the blurred image
            # `average_color` is a numpy array of [B, G, R] values
            # The result is cast to `np.uint8` to fit the standard 8-bit image format
            blurred_image[y, x] = average_color.astype(np.uint8)

    # Display the original and blurred images for comparison
    cv2.imshow('Original Image', image)
    cv2.imshow('Blurred Image (Manual Box Blur)', blurred_image)

    # Wait for a key press to close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()