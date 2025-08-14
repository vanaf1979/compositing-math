from inc.image_classes import Image

image_one = Image("./images/face.png")
image_two = Image("./images/checkout.png")

for background, foreground in zip(image_one.data(), image_two.data()):
    # Pre-multiplying the data is a good practice for accurate results
    background.premultiply()
    foreground.premultiply()

    # The Difference blend mode calculation for each color channel.
    # It subtracts the darker color from the lighter one,
    # which is the same as taking the absolute difference.
    background.r = abs(background.r - foreground.r)
    background.g = abs(background.g - foreground.g)
    background.b = abs(background.b - foreground.b)

    # Standard over operation for the alpha channel.
    # This correctly combines the transparency of the two images.
    background.a = foreground.a + background.a * (1 - foreground.a)

image_one.show(title="Difference operation")
