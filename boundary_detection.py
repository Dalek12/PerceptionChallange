
import numpy as np
import cv2
import matplotlib.pyplot as plt

def fit_line_through_centroids(centroids, img_height):
    "Fit a line through the centroids and get the top and bottom points of the line."
    x_coords = np.array([point[0] for point in centroids])
    y_coords = np.array([point[1] for point in centroids])
    slope, intercept = np.polyfit(y_coords, x_coords, 1)
    top_x = int(slope * 0 + intercept)
    bottom_x = int(slope * img_height + intercept)
    return (top_x, 0), (bottom_x, img_height)

# Load the image
img_path = 'red.png'
img = cv2.imread(img_path, cv2.IMREAD_COLOR)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Filter for red regions
lower_red = np.array([0, 0, 100])
upper_red = np.array([70, 70, 255])
mask = cv2.inRange(img, lower_red, upper_red)
res = cv2.bitwise_and(img, img, mask=mask)

# Convert to grayscale and threshold
gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
filtered_contours = [contour for contour in contours if cv2.contourArea(contour) > 100]

# Extract centroids
centroid_points = [(int(M['m10'] / M['m00']) if M['m00'] != 0 else 0, int(M['m01'] / M['m00']) if M['m00'] != 0 else 0) for M in [cv2.moments(c) for c in filtered_contours]]

# Provided centroids for left and right cones
left_cone_centroids = [centroid_points[i] for i in [1, 3, 5, 7, 9, 11, 13]]
right_cone_centroids = [centroid_points[i] for i in [0, 2, 4, 6, 8, 10, 12]]

# Fit lines through the centroids
left_line_start, left_line_end = fit_line_through_centroids(left_cone_centroids, img.shape[0])
right_line_start, right_line_end = fit_line_through_centroids(right_cone_centroids, img.shape[0])

# Draw lines on the image
img_with_final_boundaries = img_rgb.copy()
cv2.line(img_with_final_boundaries, left_line_start, left_line_end, (255, 0, 0), 2)
cv2.line(img_with_final_boundaries, right_line_start, right_line_end, (255, 0, 0), 2)

# Save the image
output_path = 'answer.png'
cv2.imwrite(output_path, cv2.cvtColor(img_with_final_boundaries, cv2.COLOR_RGB2BGR))


