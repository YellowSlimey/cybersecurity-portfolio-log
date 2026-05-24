from PIL import Image
import stepic

img = Image.open("original.png")

message = "B30_Watermark_Test"

encoded_img = stepic.encode(img, message.encode())

encoded_img.save("watermarked.png")