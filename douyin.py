from PIL import Image
import numpy as np

filepath = "husky.jpg"


img_org = Image.open(filepath).convert("RGBA")

array_orig = np.array(img_org)


arrayR = np.copy(array_orig)
arrayR[:,:, 1:3] = 0
imageR = Image.fromarray(arrayR)

arrayGB = np.copy(array_orig)
arrayGB[:,:,0] = 0
imageGB = Image.fromarray(arrayGB)

canvasR = Image.new("RGBA", img_org.size, color=(0,0,0))
canvasR.paste(imageR, (10, 10), imageR)

canvasGB = Image.new("RGBA", img_org.size, color=(0,0,0))
canvasGB.paste(imageGB,(0,0), imageGB)

result_array = np.array(canvasR) + np.array(canvasGB)
result = Image.fromarray(result_array)
result.save("result.jpg", "JPEG", quality=80, optimize=True, progressive=True)