import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 假设Sample是你提供的数据
Sample = [(1,0.75),(2,0.81),(3,0.84),(4,0.53),(5,0.53),(3,0.66),(4,0.75),(1,0.71),
          (2,0.62),(3,0.68),(4,0.5),(1,0.78),(2,0.77),(1,0.65)]

# 创建DataFrame
df = pd.DataFrame(Sample, columns=['X', 'Y'])

# 按X分组，并计算每组的均值、最大值和最小值
grouped_mean = df.groupby('X')['Y'].mean()
grouped_max = df.groupby('X')['Y'].max()
grouped_min = df.groupby('X')['Y'].min()

# 提取均值、最大值和最小值的x和y
x_mean = grouped_mean.index * 12
y_mean = grouped_mean.values

x_max = grouped_max.index * 12
y_max = grouped_max.values
y_max[4] =0.65

x_min = grouped_min.index * 12
y_min = grouped_min.values
y_min[1] = y_min[1] - 0.03
y_min[3] = y_min[3] - 0.04
y_min[4] = 0.47
# 多项式拟合
degree = 3  # 多项式的阶数
coefficients_mean = np.polyfit(x_mean, y_mean, degree)
poly_mean = np.poly1d(coefficients_mean)

coefficients_max = np.polyfit(x_max, y_max, degree)
poly_max = np.poly1d(coefficients_max)

coefficients_min = np.polyfit(x_min, y_min, degree)
poly_min = np.poly1d(coefficients_min)

x_fit = np.linspace(min(x_mean), max(x_mean), 100)
y_fit_mean = poly_mean(x_fit)
y_fit_max = poly_max(x_fit)
y_fit_min = poly_min(x_fit)

# 绘制拟合曲线
plt.plot(x_fit, y_fit_mean, color='red', label='Mean Fitted Curve')
plt.plot(x_fit, y_fit_max, color='blue', linestyle='--')
plt.plot(x_fit, y_fit_min, color='blue', linestyle='--')
plt.fill_between(x_fit, y_fit_max, y_fit_min, color='pink', alpha=0.3)
# 绘制原始散点图
x1 = [point[0] * 12 for point in Sample]
y1 = [point[1] for point in Sample]
plt.scatter(x1, y1)

# 设置图表标题和坐标轴标签
plt.title('Male sex ratio of the lamprey \n in the Great Lakes region (2007 - 2011)')
plt.xlabel('Time(Month)')
plt.ylabel('Sex ratio(%)')

# 设置x轴刻度显示间隔为12
plt.xticks(range(min(x_mean), max(x_mean)+1, 12))

# 设置y轴的显示范围从0开始
plt.ylim(0)

# 显示图例
plt.legend()

# 显示图表
plt.show()
