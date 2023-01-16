import numpy as np
a = np.array([10,20,30,40])
b = np.arange(4)
print(a,b)
c=a+b
print(c)
c=a-b
print(c)
c=a**2
print(c)
print(10*np.sin(a))
print(10*np.tan(a))

# 判断一些数符合条件
print(b<3)
print(b==3)

# numpy中的矩阵运算
a = np.array([[1,1],[2,1]])
b = np.arange(4).reshape((2,2))
print(a)
print(b)
# 把a和b逐个相乘
c = a*b
print(c)
# a和b矩阵乘法
c_dot = np.dot(a,b)
print(c_dot)
c_dot2 = a.dot(b)
print(c_dot2)

# 一些函数  可以附带参数axis  为1在列做操作为0在行做操作
print(np.min(a))
print(np.max(a))
print(np.sum(a))

print(np.min(a,axis=1))


#
A = np.arange(2,14).reshape(3,4)
print(np.argmin(A))  # 最小值的索引
print(np.argmax(A))  # 最大值索引
# 计算平均值
print(np.mean(A))
print(A.mean())

print(np.average(A))
print(np.median(A))  # 中位数

#逐步累加
print(A)
print(np.cumsum(A))

# 每两个数之间的差
print(np.diff(A))
# 非零的数
print(np.nonzero(A))
# 逐行排序
A = np.arange(20,10,-1).reshape(2,5)
print(np.sort(A))
# 矩阵转置
print(np.transpose(A))
print(A.T)


# clip规定数组的最大最小使得大于规定最大的数都等于最大，小于最小的数都等于最小
print(np.clip(A,5,9))

# 几乎所有的属性都可以使用aixs属性 0对列计算 1对行计算
