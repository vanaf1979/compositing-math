from inc.image_classes import Image

image_one = Image("./images/face.png")
image_two = Image("./images/checkout.png")

for background, foreground in zip(image_one.data(), image_two.data()):
    # Pre-multiplying the data is a good practice for accurate results
    background.premultiply()
    foreground.premultiply()

    # The Average blend mode calculation for each color channel.
    # The formula is (Foreground + Background) / 2
    background.r = (background.r + foreground.r) / 2
    background.g = (background.g + foreground.g) / 2
    background.b = (background.b + foreground.b) / 2

    # Standard over operation for the alpha channel
    # This combines the transparency of the two images correctly
    background.a = foreground.a + background.a * (1 - foreground.a)

image_one.show(title="Average operation")
