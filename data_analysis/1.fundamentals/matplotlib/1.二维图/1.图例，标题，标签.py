import matplotlib.pyplot as plt
x=[1,2,3]
y=[5,7,4]
x2=[1,2,3]
y2=[10,14,12]
#绘制折线图，每条线都有不同的label
plt.plot(x,y,label='first line')
plt.plot(x2,y2,label='second line')
# plt.legend() 生成默认图例
plt.legend()
#x轴和y轴的不同标签
plt.xlabel('Plot Number')
plt.ylabel('Important var')
#图的标题
plt.title('Interesting Graph\nCheck it out')

plt.show()