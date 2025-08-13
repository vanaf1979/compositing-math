

from inc.image_classes import Image

image_one = Image("./images/red.png")
image_two = Image("./images/blue_alpha.png")

for pixel_a, pixel_b in zip(image_one.data(), image_two.data()):

    # Final_Color=1−(1−Background_Color)/Foreground_Color

    if pixel_b.r == 0:
        pixel_a.r = 0
    else:
        pixel_a.r = 1 - (1 - pixel_a.r) / (pixel_b.r * pixel_b.a)

    if pixel_b.g == 0:
        pixel_a.g = 0
    else:
        pixel_a.g = 1 - (1 - pixel_a.g) / (pixel_b.g * pixel_b.a)

    if pixel_b.b == 0:
        pixel_a.b = 0
    else:
        pixel_a.b = 1 - (1 - pixel_a.b) / (pixel_b.b * pixel_b.a)

    pixel_a.a = max(pixel_a.a, pixel_b.a)

image_one.show(title="Lighten operation")
