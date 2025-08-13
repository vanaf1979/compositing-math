from inc.image_classes import Image

image_one = Image("./images/red.png")
image_two = Image("./images/blue_alpha.png")

for background, foreground in zip(image_one.data(), image_two.data()):

    # Straight alpha over operation.
    background.r = (foreground.r * foreground.a) + (background.r * (1 - foreground.a))
    background.g = (foreground.g * foreground.a) + (background.g * (1 - foreground.a))
    background.b = (foreground.b * foreground.a) + (background.b * (1 - foreground.a))

    # Premultiplied over operation
    background.premultiply()
    foreground.premultiply()
    background.r = foreground.r + background.r * (1 - foreground.a)
    background.g = foreground.g + background.g * (1 - foreground.a)
    background.b = foreground.b + background.b * (1 - foreground.a)


image_one.show(title="Over operation")
