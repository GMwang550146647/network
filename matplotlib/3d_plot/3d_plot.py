# 载入模块
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 创建 3D 图形对象
fig = plt.figure()
ax = Axes3D(fig)

# 生成数据
X = np.linspace(-2500, 2500, 1000)
Y = np.linspace(-7500, 500, 1000)
X, Y = np.meshgrid(X, Y)
Z = X**2 + Y**2 + 2*X*Y +10*X+40*Y
# Z = X**2 + Y**2 + 7*X*Y

# 绘制曲面图，并使用 cmap 着色
ax.plot_surface(X, Y, Z, cmap=plt.cm.winter)
ax.contour(X,Y,Z,colors='r')
plt.show()