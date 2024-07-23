import numpy as np
import matplotlib.pyplot as plt

a1 = 150
a2 = 40
a3 = 0.001

# 设定参数
G_x = lambda t, F_t_value: np.tanh(a3 * t) * (a1 + a2 * F_t_value - a1)  # 策略X的固有增长率
G_y = lambda t: np.tanh(a3 * t) * (a1)   # 策略Y的固有增长率
delta_t = 0.001  # 时间步长
time_steps = 200  # 迭代次数

params = [8.18026350e+02, 9.23795316e-01, -3.17144139e+00, -1.67278682e+01,
          1.67564710e+03, 9.55661200e-01, -2.56893632e-01, 6.23035555e-02,
          -8.65884304e+02, 9.84094894e-01, -4.60951733e-01, 2.40713429e+01]

def F_t(t):
    assert t >= 0
    while True:
        if t > 13:
            t = t - 13
        else:
            break
    return params[0] * np.sin(params[1] * t + params[2]) + params[3] +params[4] * np.sin(params[5] * t + params[6]) + params[7] +params[8] * np.sin(params[9] * t + params[10]) + params[11]


# 初始化数组
X = np.zeros(time_steps)
Y = np.zeros(time_steps)
X[0], Y[0] = 0.3, 0.7  # 初始比例

# 迭代过程
for t in range(time_steps - 1):
    F_t_value =  3  # 计算当前时间步的F_t值
    X[t + 1] = X[t] + delta_t * X[t] * (1 - X[t]) * G_x(t, F_t_value)
    Y[t + 1] = Y[t] + delta_t * Y[t] * (1 - Y[t]) * G_y(t)
    # 归一化
    total = X[t + 1] + Y[t + 1]
    X[t + 1] /= total
    Y[t + 1] /= total

# 绘制结果
plt.plot(X, label='X_t')
plt.plot(Y, label='Y_t')
plt.xlabel('Time Steps')
plt.ylabel('Strategy Proportions')
plt.title('Evolution of Strategies in a Game')
plt.legend()
plt.show()
