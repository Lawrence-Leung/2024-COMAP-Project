import numpy as np
import matplotlib.pyplot as plt
a1 = 150
a2 = 40
a3 = 0.001

# 设定参数
G_x = lambda t, F_t: np.tanh(a3 * t) * (a1 + a2 * F_t - a1)# 策略X的固有增长率
G_y = lambda t: np.tanh(a3 * t) * (a1 )   # 策略Y的固有增长率
delta_t = 0.001  # 时间步长
time_steps = 200  # 迭代次数
F_t = 3  # 可以是关于时间的任意函数
# 3.75可以


# 初始化数组
X = np.zeros(time_steps)
Y = np.zeros(time_steps)
X[0], Y[0] = 0.3, 0.7  # 初始比例

# 迭代过程
for t in range(time_steps - 1):
    X[t + 1] = X[t] + delta_t * (F_t * X[t] * (1 - X[t]) * G_x(t, F_t))
    Y[t + 1] = Y[t] + delta_t * (F_t * Y[t] * (1 - Y[t]) * G_y(t))
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
