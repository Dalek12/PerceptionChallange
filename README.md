# PerceptionChallange

![Boundary Detection](answer.png)

## Methodology

To detect the boundaries defined by the cones in the image, the following steps were taken:

1. **Color Filtering**: The image was filtered to retain only the red regions, which correspond to the cones.
2. **Grayscale and Thresholding**: The filtered image was converted to grayscale and then binarized using Otsu's thresholding.
3. **Contour Detection**: Contours in the thresholded image were identified.
4. **Contour Filtering**: Contours were filtered based on their area, aspect ratio, and position to remove unwanted detections and retain only the cones. Specifically, a contour in the top right of the image, which was not a cone, was filtered out to improve the accuracy of the boundary detection.
5. **Centroid Calculation**: The centroids of the filtered contours were computed. These centroids were used to dynamically identify the left and right cones, replacing the initial hard-coded approach.
6. **Boundary Line Fitting**: Using the centroids, two lines were fitted to represent the left and right boundaries of the path defined by the cones. The lines were adjusted based on feedback to ensure a closer fit to the cones.

## What was Tried

Initially, a direct approach of color filtering and contour detection was applied. However, some unwanted contours were also detected. To address this, additional contour filtering based on area, aspect ratio, and position was introduced. Hard-coded indices used in the first version to get a correct answer output. In order to build a more robust algorithm, inital versions were replaced with a dynamic approach based on the centroid positions of the detected cones.

## Libraries Used

- OpenCV (cv2): For image processing tasks like color filtering, contour detection, and line fitting.
- NumPy: For numerical operations and array manipulations.
- Matplotlib: For visualization purposes.

