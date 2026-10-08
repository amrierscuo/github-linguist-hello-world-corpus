import numpy as np

points = np.array([72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33], dtype=np.uint8)
assert points.shape == (13,)
print(points.tobytes().decode("ascii"))
