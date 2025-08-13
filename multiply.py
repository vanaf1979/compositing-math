from inc.image_classes import Image

image_one = Image("./images/checkout.png")
image_two = Image("./images/face.png")

for background, foreground in zip(image_one.data(), image_two.data()):

    background.premultiply()
    foreground.premultiply()

    background.r = background.r * foreground.r
    background.g = background.g * foreground.g
    background.b = background.b * foreground.b

    # Standard over operation for the alpha channel
    background.a = foreground.a + background.a * (1 - foreground.a)

image_one.show(title="Multiply operation")
