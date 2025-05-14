
import matplotlib.pyplot as plt
import matplotlib as mpl
import os
import glob
import math

# 한글 폰트 설정
mpl.rc('font', family='Malgun Gothic')
mpl.rcParams['axes.unicode_minus'] = False


with open('C:\\Users\\박나희\\Desktop\\Honing_shape_function\\contour_0.gen', 'r') as f:
    lines = f.readlines()
    
data_lines = lines[1:-2]

x = []
y = []

for line in data_lines:
    parts = line.strip().split()
    if len(parts) != 2:
        continue
    x_val, y_val = map(float, parts)
    x.append(x_val)
    y.append(y_val)
      

coordinates = list(zip(x, y))      
x_min = min(coordinates, key = lambda x: x[0])[0]
y_max = max(coordinates, key = lambda y: y[1])[1]

target = (x_min, y_max)
min_dist = float('inf')
closest_point = None

for k in coordinates:
    dist = math.dist(target, k)
    if dist < min_dist:
        min_dist = dist
        closest_point = k

print(closest_point)

# 시각화
plt.plot(x, y, linewidth=3, label='원본 곡선')
plt.axvline(x=x_min, color='red', linestyle='--', label=f'x={x_min:.2f}')
plt.axhline(y=y_max, color='green', linestyle='--', label=f'y={y_max:.2f}')
plt.scatter(*closest_point, color='blue', label='가장 가까운 점', zorder=5)
plt.xlabel("X 축")
plt.ylabel("Y 축")
plt.grid(True)
plt.legend()
plt.show()