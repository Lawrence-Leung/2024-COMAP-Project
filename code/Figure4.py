import numpy as np
import matplotlib.pyplot as plt

params = [8.18026350e+02, 9.23795316e-01, -3.17144139e+00, -1.67278682e+01,
          1.67564710e+03, 9.55661200e-01, -2.56893632e-01, 6.23035555e-02,
          -8.65884304e+02, 9.84094894e-01, -4.60951733e-01, 2.40713429e+01]


# 定义函数
f1 = lambda t, params: params[0] * np.sin(params[1] * (t-5.4) + params[2]) + params[3]
f2 = lambda t, params: params[4] * np.sin(params[5] * (t-5) + params[6]) + params[7]
f3 = lambda t, params: params[8] * np.sin(params[9] * (t-4.73) + params[10]) + params[11]


# 生成时间点
t = np.linspace(5, 12, 500)

# 计算函数值
k = 0.067
y1 = -f1(t, params) * k
y2 = -f2(t, params) * k
y3 = -f3(t, params) * k * 1.3

# 设置x轴的刻度和标签
months = ['June', 'July', 'August', 'September', 'October', 'November','December']
# 设置x轴的位置在0到7之间，对应7个月份
plt.xticks(ticks=np.linspace(5, 12, len(months)), labels=months)

# 绘制图像
plt.plot(t, y1, label='Bacteria')
plt.plot(t, y2, label='AOM & others')
plt.plot(t, y3, label='Algae')
plt.title('Equivalent Fourier components of foods')
plt.xlabel('Time(Month)')
plt.ylabel('Food amount index')
plt.legend()
plt.show()

