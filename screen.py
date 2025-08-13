from inc.image_classes import Image

image_one = Image("./images/face.png")
image_two = Image("./images/checkout.png")

for background, foreground in zip(image_one.data(), image_two.data()):

    background.premultiply()
    foreground.premultiply()

    background.r = 1 - ((1 - background.r) * (1 - foreground.r))
    background.g = 1 - ((1 - background.g) * (1 - foreground.g))
    background.b = 1 - ((1 - background.b) * (1 - foreground.b))

    # Standard over operation for the alpha channel
    background.a = foreground.a + background.a * (1 - foreground.a)

image_one.show(title="Screen operation")
