import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint



# Example values for the parameters
K = 10000  # Carrying capacity

# 涉及到h(x_t)的参数：x_t是雌雄比例，雌雄比例变动影响人口速度
mu = 0.65  # Mean of the Gaussian function
sigma = 0.22  # Standard deviation of the Gaussian function
#0.22是合理的值

# 食物：随着月份而变化
#Ft = 2.75  # Food availability at time t
a1 = 0.005  # Coefficient a1 for the linear function j(F_t)
a2 = 0  # Coefficient a2 for the linear function j(F_t)
P0 = 1030  # Initial population size    位于1000到1100之间
T = 72  # Time span for simulation

# 用于反馈调节的东西
b1 = 0.5
b2 = 800
#x_t = 0.5

# point data
# 横向
exten = 12
move = 0
# 纵向
k = 0.52
b = 0.2

def population_model(P, t, K, mu, sigma, a1, a2, b1, b2):
    """Modified Logistic Population Growth Model."""
    Ft = 10 + 10 * np.sin(t * np.pi / 6)

    x_t = (0.3 * (np.exp(-t) + 1) + 0.5 + (Ft - 10) / 100) / (b1 * np.log(b2 * (P + 0.5)))

    # Gaussian function h(x_t)
    h_xt = (1 / np.sqrt(2 * np.pi * sigma ** 2)) * np.exp(-((x_t - mu) ** 2) / (2 * sigma ** 2))

    # Linear function j(F_t)
    j_Ft = (a1 * Ft) + a2

    # Differential equation dP/dt
    dP_dt = j_Ft * P * (1 - (P / (h_xt * K)))
    return dP_dt



X = [i * exten + move for i in range(5)]
# 定义归一化函数
def normalize(data):
    min_val = min(data)
    max_val = max(data)
    result = []
    for x in data:
        nmal = (x - min_val) / (max_val - min_val)
        fix = nmal * k + b
        result.append(fix)
    return result

# 原始数据
Superior = [8.91, 5.27, 5, 4.89, 4.96]
Michigan = [42.39, 27.71, 21.41, 21.43, 22.28]
Huron = [38.58, 34.35, 29.78, 29.89, 32.60]
Erie = [1.73, 0.13, 4.67, 4.11, 3.37]
Ontario = [6.73, 8.42, 8.76, 5.6, 5.81]
small_lake = [23.42, 28.36, 19.63, 22.89, 24.64]

# 归一化处理
Superior_norm = normalize(Superior)
Michigan_norm = normalize(Michigan)
Huron_norm = normalize(Huron)
Erie_norm = normalize(Erie)
Ontario_norm = normalize(Ontario)
small_lake_norm = normalize(small_lake)


years = [2007, 2008, 2009, 2010, 2011]
# 绘制每个湖的散点图
lakes = [('Superior', Superior_norm), ('Michigan', Michigan_norm),
         ('Huron', Huron_norm), ('Erie', Erie_norm),
         ('Ontario', Ontario_norm), ('small_lake', small_lake_norm)]

'''
for i, (lake_name, lake_data) in enumerate(lakes):
    plt.figure(i + 1)  # 创建新的图形
    plt.scatter(years, lake_data)

    # 添加标题和轴标签
    plt.xticks(years)
    plt.title(f'Normalized {lake_name} Measurements')
    plt.xlabel('Measurement Number')
    plt.ylabel('Normalized Value')
'''







# Define the model



# Interface for adjusting parameters and running simulation
def simulate_population(K, mu, sigma, a1, a2, P0, T, b1, b2):
    """
    Simulate population over time with given parameters.

    Parameters:
    K (float): Carrying capacity
    mu (float): Mean of the Gaussian function
    sigma (float): Standard deviation of the Gaussian function
    Ft (float): Food availability at time t
    a1, a2 (float): Coefficients for the linear function j(F_t)
    P0 (float): Initial population size
    T (int): Time span for simulation

    Returns:
    Plot of population over time
    """
    # Time array for the simulation
    t = np.linspace(0, T, 10000)  # use 1000 points for the time array

    # Simulate using odeint
    P = odeint(population_model, P0, t, args=(K, mu, sigma, a1, a2, b1, b2))
    P_nmal = [(x - 1030) / 43 for x in P]

    # Plot the results
    plt.figure(figsize=(4, 3))
    color = '#ff7f0e'
    rgb_color = tuple(int(color[i:i + 2], 16) / 255 for i in (1, 3, 5))
    plt.plot(t, P_nmal,label='Population P(t)')
    plt.title('Ontario')
    plt.xlabel('Time (month)')
    plt.ylabel('Nomalized population')

    plt.grid(True)

    plt.scatter(X, Ontario_norm, color=rgb_color,label='Actual population')
    plt.legend()
    # 显示所有图表

    plt.show()




# This is just a demonstration, the user should use their own values for the parameters
simulate_population(K, mu, sigma, a1, a2, P0, T, b1, b2) # Uncomment this line to run the simulation with the example values

# The simulate_population function is the interface that can be used to adjust parameters and observe the effect.
# The user can call this function with different values to run their own simulation.
