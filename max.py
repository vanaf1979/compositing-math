from inc.image_classes import Image

image_one = Image("./images/red.png")
image_two = Image("./images/blue_alpha.png")

for background, foreground in zip(image_one.data(), image_two.data()):

    # Straight alpha lighten operation.
    background.r = max(background.r * background.a, foreground.r * foreground.a)
    background.g = max(background.g * background.a, foreground.g * foreground.a)
    background.b = max(background.b * background.a, foreground.b * foreground.a)

    # Premultiplied lighten operation.
    background.premultiply()
    foreground.premultiply()
    background.r = max(background.r, foreground.r)
    background.g = max(background.g, foreground.g)
    background.b = max(background.b, foreground.b)
    background.a = max(background.a, foreground.a)


image_one.show(title="Max / Lighten operation")
