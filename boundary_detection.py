
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

def extract_centroids(contours):
    "Extract centroids for given contours."
    centroids = []
    for contour in contours:
        M = cv2.moments(contour)
        if M['m00'] != 0:
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            centroids.append((cx, cy))
    return centroids

def improved_filter_contours(contours, img_shape):
    "Improved contour filtering based on area, aspect ratio, and position."
    filtered = []
    for contour in contours:
        area = cv2.contourArea(contour)
        x, y, w, h = cv2.boundingRect(contour)
        if x + w > 0.7 * img_shape[1] and y < 0.2 * img_shape[0]:
            continue
        if area > 100:
            aspect_ratio = float(w) / h
            if 0.5 < aspect_ratio < 2:
                filtered.append(contour)
    return filtered

# Load the image
img_path = 'red.png'
img = cv2.imread(img_path, cv2.IMREAD_COLOR)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Filter for red regions and find contours
lower_red = np.array([0, 0, 100])
upper_red = np.array([70, 70, 255])
mask = cv2.inRange(img, lower_red, upper_red)
res = cv2.bitwise_and(img, img, mask=mask)
gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Improved contour filtering and centroid extraction
filtered_contours = improved_filter_contours(contours, img_rgb.shape)
centroids = extract_centroids(filtered_contours)

# Sort centroids and determine left and right cones
sorted_centroids = sorted(centroids, key=lambda x: x[0])
mid_index = len(sorted_centroids) // 2
left_cone_centroids = sorted_centroids[:mid_index]
right_cone_centroids = sorted_centroids[mid_index:]

# Fit lines through the centroids
left_line_start, left_line_end = fit_line_through_centroids(left_cone_centroids, img.shape[0])
right_line_start, right_line_end = fit_line_through_centroids(right_cone_centroids, img.shape[0])

# Draw the boundary lines on the image
cv2.line(img_rgb, left_line_start, left_line_end, (255, 0, 0), 2)
cv2.line(img_rgb, right_line_start, right_line_end, (255, 0, 0), 2)
output_path = 'answer.png'
cv2.imwrite(output_path, cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR))


