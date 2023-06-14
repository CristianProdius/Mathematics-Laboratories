import numpy as np
from scipy.interpolate import bisplrep, bisplev

# Load data from file
data = np.loadtxt('C:/Users/prodi/Documents/University/Math/Mathematics-Laboratories/Number_Analyze/lab2/map.txt', delimiter=' ', skiprows=1)

# Separate known and unknown points
known_points = data[~np.isnan(data[:, 2])]
unknown_points = data[np.isnan(data[:, 2])]

# Get the coordinates and values of known points
x_known = known_points[:, 0]
y_known = known_points[:, 1]
values_known = known_points[:, 2]

# Perform scattered data interpolation
tck = bisplrep(x_known, y_known, values_known)

# Evaluate unknown values
unknown_values = bisplev(unknown_points[:, 0], unknown_points[:, 1], tck)

# Assign interpolated values to unknown points
data[np.isnan(data[:, 2]), 2] = unknown_values

# Solve linear equations
x, y = np.meshgrid(np.arange(6), np.arange(3))
A = np.vstack((x.flatten(), y.flatten(), np.ones(x.size))).T
b = data[:, 2].reshape(-1, 1)

# Handle the case when the matrix is singular
try:
    coeffs = np.linalg.solve(A, b)
    safest_path = coeffs[:2] @ np.array([[0, 1, 2, 3, 4, 5], [0, 0, 0, 0, 0, 0]])
    print("The safest path to reach the lost city is:", safest_path)
except np.linalg.LinAlgError as e:
    print("Error: Matrix is singular. Unable to compute the safest path.")
