#!/usr/bin/env python

# Gemini chat.
# https://gemini.google.com/app/cfb5981279bb0192

import cv2
import numpy as np

class Pixel:
    """
    A simple wrapper class for a pixel's data, providing intuitive
    attribute-based access to its color channels (r, g, b).

    This class is designed to make the code inside the main loop
    more readable and closer to the user's intent.
    """

    def __init__(self, *args):
        """
        Initializes the Pixel object. It can be initialized with a NumPy array
        or with individual r, g, b, (a) values.

        Args:
            *args: Either a NumPy array representing a pixel, or a sequence
                   of numeric values for the color channels (e.g., r, g, b).
        """
        if len(args) == 1 and isinstance(args[0], np.ndarray):
            self._data = args[0]
        elif len(args) >= 3 and all(isinstance(val, (int, float)) for val in args):
            # Assumes BGR format for OpenCV compatibility
            if len(args) == 3:
                self._data = np.array([args[2], args[1], args[0]], dtype=np.float32)
            elif len(args) == 4:
                self._data = np.array([args[2], args[1], args[0], args[3]], dtype=np.float32)
            else:
                raise ValueError("Pixel can be initialized with 3 or 4 channel values.")
        else:
            raise TypeError("Pixel must be initialized with a NumPy array or 3/4 numeric values.")

    @property
    def r(self):
        """Red channel value (0.0-1.0)."""
        return self._data[2]  # OpenCV loads as BGR by default

    @r.setter
    def r(self, value):
        """Sets the Red channel value."""
        self._data[2] = value

    @property
    def g(self):
        """Green channel value (0.0-1.0)."""
        return self._data[1]

    @g.setter
    def g(self, value):
        """Sets the Green channel value."""
        self._data[1] = value

    @property
    def b(self):
        """Blue channel value (0.0-1.0)."""
        return self._data[0]

    @b.setter
    def b(self, value):
        """Sets the Blue channel value."""
        self._data[0] = value

    # Add an 'a' property if the image has an alpha channel
    @property
    def a(self):
        """Alpha channel value (0.0-1.0). Returns None if no alpha channel."""
        if len(self._data) > 3:
            return self._data[3]
        return None

    @a.setter
    def a(self, value):
        """Sets the Alpha channel value."""
        if len(self._data) > 3:
            self._data[3] = value
        else:
            print("Warning: Image does not have an alpha channel to set.")

    # --- New Methods for Operator Overloading ---

    def __add__(self, other):
        """Adds two pixels, a pixel and a scalar, or a pixel and a tuple."""
        new_data = self._data + self._get_other_data(other)
        return Pixel(new_data)

    def __iadd__(self, other):
        """In-place addition: pixel_a += pixel_b"""
        self._data += self._get_other_data(other)
        return self

    def __sub__(self, other):
        """Subtracts two pixels, a pixel and a scalar, or a pixel and a tuple."""
        new_data = self._data - self._get_other_data(other)
        return Pixel(new_data)

    def __isub__(self, other):
        """In-place subtraction: pixel_a -= pixel_b"""
        self._data -= self._get_other_data(other)
        return self

    def __mul__(self, other):
        """Multiplies two pixels, a pixel and a scalar, or a pixel and a tuple."""
        new_data = self._data * self._get_other_data(other)
        return Pixel(new_data)

    def __imul__(self, other):
        """In-place multiplication: pixel_a *= pixel_b"""
        self._data *= self._get_other_data(other)
        return self

    def __truediv__(self, other):
        """Divides two pixels, a pixel and a scalar, or a pixel and a tuple."""
        # Add a small epsilon to prevent division by zero
        new_data = self._data / (self._get_other_data(other) + 1e-6)
        return Pixel(new_data)

    def __itruediv__(self, other):
        """In-place division: pixel_a /= pixel_b"""
        self._data /= (self._get_other_data(other) + 1e-6)
        return self

    def _get_other_data(self, other):
        """Helper function to get the data from 'other' regardless of its type."""
        if isinstance(other, Pixel):
            return other._data
        elif isinstance(other, (list, tuple, np.ndarray)):
            return np.array(other, dtype=np.float32)
        else:  # Assumes it's a scalar (int or float)
            return other

    def __repr__(self):
        """String representation for printing."""
        return f"Pixel(r={self.r:.2f}, g={self.g:.2f}, b={self.b:.2f})"


class Image:
    """
    A custom class to abstract image loading, pixel data, and display.
    This simplifies the demonstration of image manipulation concepts.
    """

    def __init__(self, path_to_image):
        """
        Loads an image from a given path and normalizes pixel values
        to a 0.0-1.0 range.

        Args:
            path_to_image (str): The file path to the image.
        """
        self.path = path_to_image
        self.original_image = cv2.imread(path_to_image, cv2.IMREAD_UNCHANGED)

        if self.original_image is None:
            raise FileNotFoundError(f"Error: Could not find or load image at '{path_to_image}'.")

        # Store the original dimensions to reshape the data later.
        self.height, self.width = self.original_image.shape[:2]
        self.channels = self.original_image.shape[2] if len(self.original_image.shape) > 2 else 1

        # Convert the image to float32 and normalize to a 0.0-1.0 range.
        self._data = self.original_image.astype(np.float32) / 255.0

    def data(self):
        """
        Returns the pixel data as a list of Pixel objects, allowing for
        intuitive, component-wise access (e.g., pixel.r = 0.5).

        Returns:
            list[Pixel]: A list of Pixel objects.
        """
        # We flatten the internal data for easy iteration and wrap each
        # pixel's sub-array in our custom Pixel class.
        return [Pixel(pixel) for pixel in self._data.reshape(-1, self.channels)]

    def show(self, title="Final Image"):
        """
        Displays the image based on its current internal data and handles
        window closure from a keypress.

        Args:
            title (str, optional): The title of the display window.
        """
        # Clip values to ensure they are within the valid 0.0-1.0 range.
        data_to_show = np.clip(self._data, 0.0, 1.0)

        # De-normalize and convert to uint8 for display with OpenCV.
        final_image = (data_to_show * 255).astype(np.uint8)

        cv2.imshow(title, final_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
