import pickle
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.signal import lti, impulse

with open('P1_list.pkl', 'rb') as file:
    loaded_list = pickle.load(file)

# print(len(loaded_list))

sample_list = []
for i in range(300):
    sample = loaded_list[10 * i]
    sample_list.append(sample)



# 假设 sample_list 是你的时域信号样本列表，t_samples 是对应的时间点列表
sampling_rate = 1000
t_samples = np.linspace(0, len(sample_list)/sampling_rate, len(sample_list))  # 根据采样率生成时间数组

fft_values = np.fft.fft(sample_list)
fft_freq = np.fft.fftfreq(len(sample_list), 1/sampling_rate)

# 只需要取FFT的一半（正频率部分）
n = len(sample_list) // 2

# 定义二阶系统的时域响应函数
def second_order_response(t, omega_n, zeta):
    # 创建一个二阶系统
    system = lti([omega_n**2], [1, 2*zeta*omega_n, omega_n**2])
    # 计算系统的脉冲响应
    t_out, response = impulse(system, T=t)
    return response

# 使用curve_fit进行参数拟合
popt, pcov = curve_fit(second_order_response, t_samples, sample_list, p0=[1, 0.1])

# 输出拟合得到的自然频率和阻尼比
omega_n, zeta = popt
print(f"Natural frequency (omega_n): {omega_n}")
print(f"Damping ratio (zeta): {zeta}")

# 输出LaTeX格式的传递函数
latex_tf = f"\\frac{{{omega_n}^2}}{{s^2 + 2 \\cdot {zeta} \\cdot {omega_n} \\cdot s + {omega_n}^2}}"
print(latex_tf)
# plt.scatter(fft_freq[:n], np.abs(fft_values[:n]), label='FFT of the signal')

# 生成拟合曲线的数据
fitted_response = second_order_response(t_samples, omega_n, zeta)

# 绘制拟合曲线
plt.plot(t_samples, fitted_response, label='Fitted Curve', color='blue')

# 设置图例
plt.legend()

# 设置标题和坐标轴标签
plt.title('Second Order System Response')
plt.xlabel('Time (seconds)')
plt.ylabel('Response')

# 显示图表
plt.grid(True)
plt.show()

import cmath

def solve_quadratic_equation(a, b, c):
    # 计算判别式
    discriminant = cmath.sqrt(b**2 - 4*a*c)
    # 计算两个解
    x1 = (-b + discriminant) / (2*a)
    x2 = (-b - discriminant) / (2*a)
    return x1, x2

# 输入系数
a = 1
b = 2 * zeta * omega_n
c = omega_n ** 2

# 确保a不
solutions = solve_quadratic_equation(a, b, c)

print(f"x1 = {solutions[0]}")
print(f"x2 = {solutions[1]}")
