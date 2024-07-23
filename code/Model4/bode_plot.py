import pickle
import numpy as np
import matplotlib.pyplot as plt


with open('P1_list.pkl', 'rb') as file:
    loaded_list = pickle.load(file)

print(len(loaded_list))

sample_list = []
for i in range(300):
    sample = loaded_list[5 * i]
    sample_list.append(sample)




# 假设 sample_list 是你的时域信号样本列表
# 替换为你的时域信号数据
sampling_rate = 2000  # 你的采样率

# 计算傅里叶变换
n = len(sample_list)
freq_response = np.fft.fft(sample_list)
frequencies = np.fft.fftfreq(n, d=1/sampling_rate)

# 频率响应的幅度和相位
magnitude = 20 * np.log10(np.abs(freq_response))
phase = np.angle(freq_response, deg=True)

# 选择正频率
pos_freq = frequencies > 0
frequencies = frequencies[pos_freq]
magnitude = magnitude[pos_freq]
phase = phase[pos_freq]

# 画伯德图
plt.figure()
plt.subplot(2, 1, 1)
plt.semilogx(frequencies, magnitude)  # 幅度图
plt.title('Bode Magnitude Plot')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude [dB]')

plt.subplot(2, 1, 2)
plt.semilogx(frequencies, phase)  # 相位图
plt.title('Bode Phase Plot')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Phase [degrees]')

plt.tight_layout()
plt.show()
