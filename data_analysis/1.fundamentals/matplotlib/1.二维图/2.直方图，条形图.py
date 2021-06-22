import matplotlib.pyplot as plt
####1.plt.bar()是绘制条形图的函数
#1有5个，3有2个，5有7个。。。。
plt.bar([1, 3, 5, 7, 9], [5, 2, 7, 8, 2], label="Example one")
plt.bar([2, 4, 6, 8, 10], [8, 6, 2, 5, 6], label="Example two", color='g') # g 为绿色， b 为蓝色， r 为红色
plt.legend()
plt.xlabel('bar number')
plt.ylabel('bar height')
plt.title('Epic Graph\nAnother Line! Whoa')
plt.show()
####2.直方图
import matplotlib.pyplot as plt
# 例如年龄的散点集
population_ages = [22, 55, 62, 45, 21, 22, 34, 42, 42, 4, 99, 102, 110, 120, 121, 122, 130, 111, 115, 112, 80, 75, 65,
                   54, 44, 43, 42, 48]
#统计年龄在这些区间的个数
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]
plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()