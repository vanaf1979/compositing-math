from inc.image_classes import Image

image_one = Image("./images/face.png")
image_two = Image("./images/checkout.png")

for pixel_a, pixel_b in zip(image_one.data(), image_two.data()):

    pixel_a.r = pixel_a.r * pixel_b.r
    pixel_a.g = pixel_a.g * pixel_b.g
    pixel_a.b = pixel_a.b * pixel_b.b
    pixel_a.a = pixel_a.a * pixel_b.a

image_one.show(title="BImage multiplication")
