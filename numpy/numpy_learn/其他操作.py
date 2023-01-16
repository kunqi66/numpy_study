import numpy as np
A = np.arange(3,15).reshape((3,4))
# 迭代A的行
for row in A:
    print(row)


# 迭代列
for low in A.T:
    print(low)

# 返回一个A变为一行的array
print(A.flatten())

for a in A.flat:   # 把A变为一行迭代
    print(a)

# 数组array的合并

A = np.array([1,1,1])
B = np.array([2,2,2])

# 给矩阵新增维度
A1 = A[:,np.newaxis]
B1 = B[:,np.newaxis]

print(A1)
print(B1)


E = np.hstack((A1,B1))
print(E)


print(A1.shape,B1.shape)


C = np.vstack((A,B))  # 竖向方向合并
print(C)
D = np.hstack((A,B))  # 横向方向合并
print(D)

# 多个数组进行拼接
C = np.concatenate((A1,B1,B1,A1),axis=1)  #竖向拼接aixs=0  横向合并aixs=1
print(C)




# 对矩阵进行分割
A = np.arange(12).reshape(3,4)
print(A)

print(np.split(A,3,axis=0))  # 分割，axis维度参数

# 不等量分割
print(np.array_split(A,3,axis=1))

# 上面的不等分为 2 1 1 分割
# 竖向横向分割
np.vstack(A,3)
np.hsplit(A,2)


# 复制
# 直接赋值
a = A  # 属于赋值引用指向同一个array
a = A.copy()   # 仅仅只是赋值
