from inc.image_classes import Image

image_one = Image("./images/red.png")
image_two = Image("./images/blue_alpha.png")

for pixel_a, pixel_b in zip(image_one.data(), image_two.data()):
    # Fg_Color * Fg_Alpha + Bg_Color * (1 - Fg_Alpha)
    pixel_a.r = (pixel_b.r * pixel_b.a) + (pixel_a.r * ( 1 - pixel_b.a))
    pixel_a.g = (pixel_b.g * pixel_b.a) + (pixel_a.g * ( 1 - pixel_b.a))
    pixel_a.b = (pixel_b.b * pixel_b.a) + (pixel_a.b * ( 1 - pixel_b.a))
    # pixel_a.a += pixel_b.a

image_one.show(title="Over")
