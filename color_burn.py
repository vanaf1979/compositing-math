from inc.image_classes import Image

EPSILON = 1e-6

image_one = Image("./images/checkout.png")
image_two = Image("./images/face.png")

for background, foreground in zip(image_one.data(), image_two.data()):

    background.r = 1 - (1 - background.r) / (foreground.r + EPSILON) if foreground.r > 0 else 0
    background.g = 1 - (1 - background.g) / (foreground.g + EPSILON) if foreground.g > 0 else 0
    background.b = 1 - (1 - background.b) / (foreground.b + EPSILON) if foreground.b > 0 else 0

    # Standard over operation for the alpha channel
    background.a = foreground.a + background.a * (1 - foreground.a)

    background.premultiply()

image_one.show(title="Lighten operation")
