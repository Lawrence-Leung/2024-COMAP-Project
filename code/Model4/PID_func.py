import pickle
import numpy as np
from scipy.fft import fft
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from scipy.signal import freqs

with open('P1_list.pkl', 'rb') as file:
    loaded_list = pickle.load(file)

# print(len(loaded_list))

sample_list = []
for i in range(300):
    sample = loaded_list[10 * i]
    sample_list.append(sample)
# 采样频率
fs = 1000  # 1 Hz, 你需要根据实际情况修改这个值

# FFT转换
N = len(sample_list)
freq = np.fft.fftfreq(N, 1/fs)
sample_fft = fft(sample_list)

# 定义传递函数模型
def transfer_function_model(s, kp, b1, b2, b3, b4):
    numerator = kp * (b1*s + 1) * (b3*s + 1)
    denominator = (s**2 - 34.16*s + 400) * (b2*s + 1) * (b4*s + 1)
    return numerator / denominator

# 由于FFT返回复数，我们使用其幅度
sample_fft_magnitude = np.abs(sample_fft)

# 拟合频域数据到传递函数模型
# 注意：我们需要一个合适的初始猜测参数集，这里我只是随意设置了一些值
initial_guess = [1, 1, 1, 1, 1]
params, _ = curve_fit(transfer_function_model, freq, sample_fft_magnitude, p0=initial_guess)

# 拟合得到的参数
kp, b1, b2, b3, b4 = params

# 输出为LaTeX格式
latex_string = f"\\frac{{{kp}}}{{s^2 + {-34.16} \\times s + {400}}} \\times \\left(\\frac{{{b1} \\times s + 1}}{{{b2} \\times s + 1}} \\times \\frac{{{b3} \\times s + 1}}{{{b4} \\times s + 1}}\\right)"
print(latex_string)

positive_freq = freq[:N//2]
sample_fft_magnitude = np.abs(sample_fft)[:N//2]
fitted_curve = transfer_function_model(positive_freq, kp, b1, b2, b3, b4)
plt.figure(figsize=(10, 6))
plt.scatter(positive_freq, sample_fft_magnitude, color='blue', label='FFT Magnitude')
plt.plot(positive_freq, fitted_curve, color='red', label='Fitted Curve')
plt.title('Frequency Domain Response and Fitted Curve')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.legend()
plt.grid(True)



b = [kp*b1*b3, kp*(b1+b3), kp]
a1 = -34.16
a2 = 400
a = [1, a1+b2+b4, a2+a1*b2+a1*b4+b1*b3+b2*b3, a2*(b2+b4)+a1*b2*b4, a2*b2*b4]

# 计算传递函数在一系列对数间隔的频率上的响应
w, h = freqs(b, a, worN=np.logspace(-1, 1, 500))

# 创建新的matplotlib图形
plt.figure(figsize=(12, 6))

# 绘制幅度响应
plt.subplot(2, 1, 1)
plt.semilogx(w, 20 * np.log10(np.abs(h)))
plt.title('Bode Plot of the Fitted Transfer Function')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Amplitude [dB]')
plt.grid(which='both', axis='both')

# 绘制相位响应
plt.subplot(2, 1, 2)
angles = np.unwrap(np.angle(h))
plt.semilogx(w, np.degrees(angles))
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Phase [degrees]')
plt.grid(which='both', axis='both')

# 显示图形
plt.tight_layout()
plt.show()