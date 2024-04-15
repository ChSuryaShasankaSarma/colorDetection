# Color Detection in Images using OpenCV and K-Means Clustering
This repository contains code to perform color detection in images using the OpenCV library and K-Means clustering algorithm. The code identifies the dominant colors in an image and provides their names along with a visualization of the color palette.
## Table of Contents
1. Setup 
2. Usage
3. Code Explanation
   > Loading Image ;
   > K-Means Clustering ;
   > Finding Nearest Color Name ;
   >  Visualization ;
4. Sample Output
5. References

## Setup <a name="setup"></a>
1. Clone this repository to your local machine:
 ```ruby
 git clone https://github.com/yourusername/color-detection.git
```
 2. Navigate to the project directory:
```ruby
cd color-detection
```
3. Ensure you have Python installed on your system along with the required libraries. You can install the dependencies using pip:
   ```ruby
   pip install -r requirements.txt
   ```
## Usage <a name="usage"></a>
1. Place the image file you want to analyze in the project directory.
2. Open a terminal or command prompt and run the Python script:
   ```ruby
   python color_detection.py
   ```
3. The script will display the dominant colors detected in the image along with their names and a visualization of the color palette.
   
## Code Explanation <a name="code-explanation"></a>
### Loading Image <a name="loading-image"></a>
The script first loads the image using the OpenCV library:
```ruby
img = cv2.imread(image_path)
```
### K-Means Clustering <a name="k-means-clustering"></a>
Next, it performs K-Means clustering to find the dominant colors in the image:
```ruby
_, labels, centers = cv2.kmeans(pixels.astype(np.float32), num_colors, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

```
### Finding Nearest Color Name <a name="finding-nearest-color-name"></a>
After clustering, it finds the nearest color name for each dominant color using a predefined color names dataset:
```ruby
nearest_color_names = [find_nearest_color(center) for center in centers.astype(np.uint8)]
```

### Visualization <a name="visualization"></a>
Finally, it visualizes the dominant colors in the image by drawing rectangles for each color in a color palette image:
```runy
palette[:, i*palette_width:(i+1)*palette_width] = color
```
### Sample Output <a name="sample-output"></a>
```ruby
Dominant Color 1: BGR(128, 72, 47), Name: saddlebrown
Dominant Color 2: BGR(251, 251, 235), Name: floralwhite
Dominant Color 3: BGR(75, 50, 38), Name: darkslategray
Dominant Color 4: BGR(95, 75, 67), Name: darkolivegreen
Dominant Color 5: BGR(249, 233, 144), Name: khaki
Dominant Color 6: BGR(172, 91, 55), Name: sienna
Dominant Color 7: BGR(123, 101, 94), Name: dimgray
Dominant Color 8: BGR(171, 119, 97), Name: indianred
Dominant Color 9: BGR(241, 176, 84), Name: sandybrown
Dominant Color 10: BGR(233, 122, 52), Name: peru
```
![image](https://github.com/ChSuryaShasankaSarma/colorDetection/assets/167118995/2d0e03bf-ba42-43c0-8d6e-715a40bd1801)

![image](https://github.com/ChSuryaShasankaSarma/colorDetection/assets/167118995/1f308c51-56a2-45b2-a716-6f3973965489)

### References <a name="references"></a>
@ OpenCV Documentation: https://docs.opencv.org/

@ Webcolors Documentation: https://webcolors.readthedocs.io/
