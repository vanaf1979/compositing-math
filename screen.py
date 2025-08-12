from inc.image_classes import Image

image_one = Image("./images/face.png")
image_two = Image("./images/checkout.png")

for pixel_a, pixel_b in zip(image_one.data(), image_two.data()):
    # The Screen blend mode formula is: Result = 1 - ((1 - A) * (1 - B))
    pixel_a.r = 1 - ((1 - pixel_a.r) * (1 - pixel_a.r))
    pixel_a.g = 1 - ((1 - pixel_a.g) * (1 - pixel_b.g))
    pixel_a.b = 1 - ((1 - pixel_a.b) * (1 - pixel_b.b))

    # Screen alpha
    # pixel_a.a = 1 - ((1 - pixel_a.a) * (1 - pixel_b.a))

    # The maximum alpha
    # pixel_a.a = max(pixel_a.a, pixel_b.a)

    # The A over B Composite
    pixel_a.a = (pixel_a.a + pixel_b.a) * (1 - pixel_a.a)

image_one.show(title="Screen Blend Mode")
