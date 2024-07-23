import sympy as sp
import matplotlib.pyplot as plt

# 定义变量
s = sp.symbols('s')

# 定义函数
numerator = (2.474799529659196 * (6443.725057225905 * s + 1) * (6444.09141430197 * s + 1))
denominator = ((s**2 - 34.16 * s + 400) * (-0.33097075038037593 * s + 1) * (-232.54641661514898 * s + 1))
f = numerator / denominator

# 计算零点和极点
zeros = sp.solve(sp.numer(f), s)
poles = sp.solve(sp.denom(f), s)

# 转换为浮点数
zeros = [sp.N(z) for z in zeros]
poles = [sp.N(p) for p in poles]

# 打印零点和极点
print("零点:", zeros)
print("极点:", poles)

# 绘制散点图
plt.figure(figsize=(10, 6))
plt.scatter([sp.re(z) for z in zeros], [sp.im(z) for z in zeros], color='blue', label='Zeros')
plt.scatter([sp.re(p) for p in poles], [sp.im(p) for p in poles], marker='x',color='red', label='Poles')
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.title('Zeros and Poles of the Function')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid()
plt.legend()
plt.show()
