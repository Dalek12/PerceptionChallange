# PerceptionChallange

![Answer Image](answer.png)

## Methodology

The goal was to detect the boundaries of a straight path defined by red cones in an image. The following methodology was employed:

1. **Color Filtering:** The image was filtered to only include regions with a strong red color component, which is characteristic of the cones.
2. **Thresholding:** The filtered image was converted to grayscale and subsequently to binary using Otsu's thresholding.
3. **Contour Detection:** Contours were detected in the binary image. Small contours, likely arising from noise, were filtered out.
4. **Centroid Calculation:** The centroids of the identified contours were computed.
5. **Line Fitting:** Based on the centroids of the left and right cones, lines were fit to represent the path boundaries.
6. **Line Drawing:** The computed lines were drawn on the original image to visualize the path boundaries.

## What Was Tried and Why It Didn't Work Initially

1. **Simple Color Filtering:** Initial attempts at color filtering did not isolate the red cones effectively. Adjustments in the color ranges were necessary to accurately target the red cones.
2. **Vertical Lines Based on Centroids:** Initially, straight vertical lines were drawn based on the centroids of the leftmost and rightmost detected red cones. This approach did not account for the general direction of the cones, leading to misalignment.
3. **Line Fitting:** An attempt to fit lines to the centroids of the detected cones was made. However, the initial fitting method did not yield accurate results, and adjustments were required.

## Libraries Used

- OpenCV (cv2): For image processing tasks such as color filtering, contour detection, and line fitting.
- NumPy: For numerical operations.
- Matplotlib: For visualizing the results.
