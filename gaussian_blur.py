import cv2
import numpy as np

# Load the image
# Replace 'your_image.jpg' with the path to your image
image = cv2.imread('./images/checkout.png')

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load image.")
else:
    # Get the dimensions of the image
    height, width, channels = image.shape

    # Define the kernel size for the blur
    # A 5x5 kernel is a common choice, but you can adjust this value
    kernel_size = 5

    # Define the standard deviation (sigma) for the Gaussian function
    # A larger sigma results in a more significant blur
    sigma = 5.0

    # Create an output image array with the same dimensions, initialized to zeros
    blurred_image = np.zeros_like(image, dtype=np.float32)

    # --- Step 1: Manually Generate the Gaussian Kernel ---
    # The kernel is a matrix of weights that will be applied to the image
    kernel = np.zeros((kernel_size, kernel_size), dtype=np.float32)
    center = kernel_size // 2

    # Iterate through the kernel and calculate the weight for each element
    # The Gaussian formula is used: G(x, y) = 1 / (2 * pi * sigma^2) * exp(-(x^2 + y^2) / (2 * sigma^2))
    for i in range(kernel_size):
        for j in range(kernel_size):
            x = i - center
            y = j - center
            kernel[i, j] = np.exp(-(x**2 + y**2) / (2 * sigma**2))

    # Normalize the kernel so that the sum of all its elements is 1
    # This is crucial for maintaining the image's overall brightness
    kernel /= np.sum(kernel)

    # --- Step 2: Convolve the Image with the Kernel ---
    # Padding is added to the image to handle the edges, so the kernel doesn't go out of bounds
    pad_size = kernel_size // 2
    padded_image = np.pad(image, ((pad_size, pad_size), (pad_size, pad_size), (0, 0)), mode='reflect')

    # Iterate through each pixel of the original image
    for y in range(height):
        for x in range(width):
            # For each pixel, get the region of interest (ROI) from the padded image
            # This ROI is the area the kernel will be applied to
            roi = padded_image[y : y + kernel_size, x : x + kernel_size]

            # Apply the kernel to the ROI for each color channel (B, G, R)
            # `np.sum()` is used to calculate the weighted sum of pixels
            # The `roi * kernel[:, :, np.newaxis]` performs an element-wise multiplication
            # of the ROI and the kernel for each channel
            for c in range(channels):
                blurred_image[y, x, c] = np.sum(roi[:, :, c] * kernel)

    # Convert the blurred image back to an 8-bit integer format
    blurred_image = blurred_image.astype(np.uint8)

    # Display the original and blurred images
    cv2.imshow('Original Image', image)
    cv2.imshow('Blurred Image (Manual Gaussian Blur)', blurred_image)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()