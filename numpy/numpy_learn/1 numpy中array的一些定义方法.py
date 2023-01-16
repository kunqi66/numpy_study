import numpy as np

# 把一个列表变成矩阵
array = np.array([[1,2,3],[4,5,6]])
# 输出矩阵
print(array)
# 输出数组的维度
print('number of dim',array.ndim)
# 输出数组的形状几行几列
print('shape',array.shape)
# 数组的大小，有多少数字
print('size',array.size)
# 直接生成固定行列的全零数组
a = np.zeros((5,6))
print(a)
# 生成接近于0的数组
arr= np.empty((3,4))
print(arr)
# 生成固定步长数组
arr= np.arange(10,20,2)
print(arr)
# 设置数组中的数字格式  并重新定义他的长和宽
arr= np.array([1,2,3],dtype=int).reshape((3,1))
print(arr)
print(arr.dtype)
# 定义线段  生成两个数字之间，固定段数的数组
arr =np.linspace(1,10,6).reshape(2,3)
print(arr)
# 随机生成array
a = np.random.random((2,2))
print(a)


