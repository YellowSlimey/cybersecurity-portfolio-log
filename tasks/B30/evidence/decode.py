from PIL import Image
import stepic

imgName = input("enter image name: ")

img = Image.open(f"{imgName}.png")
print(stepic.decode(img))