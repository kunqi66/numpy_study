import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3,3,50)   # 划分数组
y1 = 2*x+1
y2 = x**2
plt.figure()     # 创建一个figure 按顺序创建添加 创建语句后面的语句为这个figure添加东西
plt.plot(x,y1)

plt.figure(num=3,figsize=(8,5))  # 为figure添加参数，num为名字尾缀，后面为大小

plt.plot(x,y2)
plt.plot(x,y1,linewidth=1.0,linestyle='--')   # 对图像进行设置

# 对坐标轴的设置
plt.xlim((-1,2))   # 对x轴范围的设置
plt.ylim((-2,3))   # 对y轴范围的设置
plt.xlabel("i am x")  # 对名称的设置
plt.ylabel("i am y")

# 对数字范围，粒度的设置
new_ticks = np.linspace(-1,2,5)  # 用numpy生成数组
plt.xticks(new_ticks)
# 对相应的数字位置进行字体设置
plt.yticks([-2,-1.8,-1,1.22,3,],
           [r'$really\ bad$',r'$bad$',r'$normal$',r'$good$',r'$really\ good$'])


# 设置四条边框和坐标轴

# gca = 'get current axis'
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 设置x轴和y轴
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# 设置x，y轴位置
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))


plt.show()



