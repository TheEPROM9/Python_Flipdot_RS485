from PIL import Image
import numpy as np

# Open the imagen
img = Image.open("hozline.bmp")

# Convert the image to a NumPy array
arr = np.array(img)

# Print the array
with open("hozline.txt", "w") as f:
	for i in range(arr.shape[0]):
		for j in range(arr.shape[1]):
			if arr[i, j] == 0:
				f.write(f"	image[{i}, {j}] = False\n")
			else:
				f.write(f"	image[{i}, {j}] = True\n")
