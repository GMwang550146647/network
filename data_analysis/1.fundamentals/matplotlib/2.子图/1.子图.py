import random
import matplotlib.pyplot as plt
from matplotlib import style
def create_plots():
    xs = []
    ys = []

    for i in range(10):
        x = i
        y = random.randrange(10)

        xs.append(x)
        ys.append(y)
    return xs, ys


style.use('fivethirtyeight')
fig = plt.figure()
ax1 = plt.subplot2grid((6,1), (0,0), rowspan=1, colspan=1)
ax2 = plt.subplot2grid((6,1), (1,0), rowspan=4, colspan=1)
ax3 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1)
x1,y1=create_plots()
x2,y2=create_plots()
x3,y3=create_plots()
ax1.plot(x1,y1)
ax2.plot(x2,y2)
ax3.plot(x3,y3)
plt.show()
# 6
# x1：
#
# colspan = 1
# (0, 0) + -----------+
#        | ax1        | rowspan = 1
# (1, 0) + -----------+
#        |            |
#        | ax2        | rowspan = 4
#        |            |
#        |            |
# (5, 0) + -----------+
#        | ax3        | rowspan = 1
#         +-----------+
