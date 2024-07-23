import random

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import norm

months = np.arange(1, 14, 1)  # 5月到次年5月
food_of_month = [14.7, 20.6, 13.2, 10.6, 12.5, 13.6, 5.1, 3, 0.9, 1, 0.65, 0, 9]

# 确保数据点的个数和月份相同
assert len(food_of_month) == 13, "确保数据点的数量是12个月的数据"

# 定义拟合函数，这里使用三个正弦波的总和
def fit_func(x, A1, B1, C1, D1, A2, B2, C2, D2, A3, B3, C3, D3):
    sum_value = A1 * np.sin(B1 * x + C1) + D1 + A2 * np.sin(B2 * x + C2) + D2 + A3 * np.sin(B3 * x + C3) + D3
    g_d = norm(loc=1, scale=0.8752).rvs()
    return sum_value

def cal_sigma():
    sum_square = 0
    for i in range(13):
        y_real = food_of_month[i]
        y_pred = fit_func(i+1,*params)
        # print(y_real,y_pred, y_real - y_pred)
        sum_square = sum_square + (y_real - y_pred) ** 2
    # print(sum_square)

    sigma = np.sqrt(sum_square / 13)

    return sigma

# 初始参数猜测，可能需要根据实际数据进行调整
guess = [10, 2*np.pi/12, 0, 0, 5, 2*np.pi/12, 0, 0, 3, 2*np.pi/12, 0, 0]

# 使用curve_fit进行拟合，增加最大函数评估次数
params, params_covariance = curve_fit(fit_func, months, food_of_month, p0=guess, maxfev=100000)

# 打印拟合参数
print(params)

# 使用拟合参数绘制结果
plt.figure(figsize=(10, 5))
plt.scatter(months, food_of_month, label='Food abundance')

# 创建一个更密集的月份数组来绘制平滑曲线
fine_months = np.linspace(1, 13, 300)
plt.plot(fine_months, fit_func(fine_months, *params), label='Fitted function')
print(cal_sigma())
labels = ['May','June','July','August','September','October','November','December','January','February','March','April','May']
for i in range(len(food_of_month)):
    if i == 0:
        plt.text(i + 1.03, food_of_month[i] + 0.07, labels[i], fontsize=9, ha='right', va='bottom')
        continue
    if i == 9:
        plt.text(i + 1.23, food_of_month[i] - 1.2, labels[i], fontsize=9, ha='right', va='bottom')
        continue
    else:
        plt.text(i + 0.93, food_of_month[i] + 0.07, labels[i], fontsize=9, ha='right', va='bottom')


plt.legend(loc='best')
plt.xlabel('Month',fontsize=11)
plt.ylabel('Food Amount',fontsize=11)
plt.title('Temporal Curve of Food Abundance')
plt.tick_params(axis='x',          # 应用到x轴
                which='both',      # 应用到所有刻度（主刻度和次刻度）
                bottom=False,      # 隐藏底部刻度线
                top=False,         # 隐藏顶部刻度线
                labelbottom=False) # 隐藏刻度标签
#plt.xlim([5, max(months)])

plt.show()
