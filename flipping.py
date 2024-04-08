#flipping the image

from PIL import Image

#opening the image
img = Image.open('download.jpeg')

#transposing
transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT)

#to human understandable format
transposed_img.save('corrected.jpeg')

print("done flipping")
