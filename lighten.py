from inc.image_classes import Image

image_one = Image("./images/red.png")
image_two = Image("./images/blue_alpha.png")

for pixel_a, pixel_b in zip(image_one.data(), image_two.data()):

    # Straight alpha lighten operation.
    pixel_a.r = max(pixel_a.r * pixel_a.a, pixel_b.r * pixel_b.a)
    pixel_a.g = max(pixel_a.g * pixel_a.a, pixel_b.g * pixel_b.a)
    pixel_a.b = max(pixel_a.b * pixel_a.a, pixel_b.b * pixel_b.a)

    # Premultiplied lighten operation.
    pixel_a.premultiply()
    pixel_b.premultiply()
    pixel_a.r = max(pixel_a.r, pixel_b.r)
    pixel_a.g = max(pixel_a.g, pixel_b.g)
    pixel_a.b = max(pixel_a.b, pixel_b.b)
    pixel_a.a = max(pixel_a.a, pixel_b.a)


image_one.show(title="Lighten operation")
