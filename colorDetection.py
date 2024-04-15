from google.colab.patches import cv2_imshow
import cv2
import numpy as np
import webcolors

# Load image
image_path = '/content/drive/MyDrive/arch/fire_and_smoke/Testing/fire/abc169.jpg'
img = cv2.imread(image_path)

# Function to find the nearest color name for a given BGR value
def find_nearest_color(bgr):
    min_dist = float('inf')
    nearest_color_name = None
    for hex_value, name in x11_colors.items():
        rgb = webcolors.hex_to_rgb(hex_value)
        dist = np.linalg.norm(np.array(bgr) - np.array(rgb[::-1]))  # Convert RGB to BGR
        if dist < min_dist:
            min_dist = dist
            nearest_color_name = name
    return nearest_color_name

# Load X11 color names
x11_colors = webcolors.CSS3_HEX_TO_NAMES

# Resize image for faster processing if needed
# img = cv2.resize(img, None, fx=0.5, fy=0.5)

# Reshape the image to 2D array of pixels
pixels = img.reshape(-1, 3)

# Perform K-means clustering to find the dominant colors
num_colors = 10
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, 0.1)
_, labels, centers = cv2.kmeans(pixels.astype(np.float32), num_colors, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# Convert centers to uint8 and find the nearest color name for each center
nearest_color_names = [find_nearest_color(center) for center in centers.astype(np.uint8)]

# Display the dominant colors and their names
for i, color in enumerate(centers.astype(np.uint8)):
    print(f"Dominant Color {i+1}: BGR({color[2]}, {color[1]}, {color[0]}), Name: {nearest_color_names[i]}")

# Create a blank image for the color palette visualization
palette_width = 50
palette_height = 300
palette = np.zeros((palette_height, len(centers) * palette_width, 3), dtype=np.uint8)

# Draw rectangles for each dominant color in the palette
for i, color in enumerate(centers.astype(np.uint8)):
    palette[:, i*palette_width:(i+1)*palette_width] = color

# Display the image and color palette
cv2_imshow(img)
cv2_imshow(palette)
