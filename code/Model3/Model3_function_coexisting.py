'''
请你帮我把以下这些段latex数学公式转换成python代码
\[\begin{align}
  & {{P}_{1a}}=\int_{t-48}^{t}{\frac{\partial {{P}_{1}}}{\partial t}}dt \\
 & {{P}_{1b}}=\int_{t-60}^{t-48}{\frac{\partial {{P}_{1}}}{\partial t}}dt \\
 & {{P}_{1c}}=\int_{t-84}^{t-60}{\frac{\partial {{P}_{1}}}{\partial t}}dt \\
 & {{P}_{1}}={{P}_{1a}}+{{P}_{1b}}+{{P}_{1c}} \\
 & \frac{\partial {{P}_{1}}}{\partial t}={{j}_{1}}({{F}_{t}})\cdot {{P}_{1}}(1-\frac{{{P}_{1}}}{h({{x}_{t}}^{\prime })\cdot {{K}_{1}}})+\left( {{\alpha }_{21a}}{{P}_{2}}{{P}_{1a}}+{{\alpha }_{21c}}{{P}_{2}}{{P}_{1c}}+{{\alpha }_{31}}{{P}_{3}}{{P}_{1}} \right) \\
 & \frac{\partial {{P}_{2}}}{\partial t}={{j}_{2}}({{F}_{t}})\cdot {{P}_{2}}(1-\frac{{{P}_{2}}}{{{K}_{2}}})+\left( {{\alpha }_{1c2}}{{P}_{1c}}{{P}_{2}}+{{\alpha }_{1a2}}{{P}_{1a}}{{P}_{2}}+{{\alpha }_{32}}{{P}_{3}}{{P}_{2}} \right) \\
 & \frac{\partial {{P}_{2}}}{\partial t}={{j}_{3}}\cdot {{P}_{3}}(1-\frac{{{P}_{3}}}{{{K}_{3}}})+\left( {{\alpha }_{13}}{{P}_{1}}{{P}_{2}}+{{\alpha }_{23}}{{P}_{3}}{{P}_{2}} \right) \\
\end{align}\]
其中，{{j}_{1}}({{F}_{t}})，{{j}_{2}}({{F}_{t}})，h({{x}_{t}})这三个函数已经写好在如下的python代码中：
def j1_ft(t,w, b):
    Ft = 10 + 10 * np.sin(t * np.pi / 6)
    j_Ft = (w * Ft) + b

    return j_Ft

def j2_ft(t,w, b):
    Ft = 10 + 10 * np.sin(t * np.pi / 6)
    j_Ft = (w * Ft) + b

    return j_Ft

def h_xt(t,sigma,mu,P, b1, b2):
    Ft = 10 + 10 * np.sin(t * np.pi / 6)
    x_t = (0.3 * (np.exp(-t) + 1) + 0.5 + (Ft - 10) / 100) / (b1 * np.log(b2 * (P + 0.5)))
    h_xt = (1 / np.sqrt(2 * np.pi * sigma ** 2)) * np.exp(-((x_t - mu) ** 2) / (2 * sigma ** 2))

    return h_xt
'''
import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

# Model2 参数：h_xt
# Example values for the parameters


# 涉及到h(x_t)的参数：x_t是雌雄比例，雌雄比例变动影响人口速度
mu = 0.65  # Mean of the Gaussian function
sigma = 0.22  # Standard deviation of the Gaussian function
#0.22是合理的值

# 食物：随着月份而变化
#Ft = 2.75  # Food availability at time t
a1 = 0.005  # Coefficient a1 for the linear function j(F_t)
a2 = 0  # Coefficient a2 for the linear function j(F_t)
P0 = 1030  # Initial population size    位于1000到1100之间
T = 120  # Time span for simulation

# 用于反馈调节的东西
b1 = 0.5
b2 = 800
#x_t = 0.5


def j1_ft(t):
    Ft = np.sin(t * np.pi / 6)
    #Ft = 1
    j_Ft = (w_j1_ft * Ft) + b_j1_ft
    return j_Ft

def j2_ft(t):
    Ft = np.sin(t * np.pi / 6)
    #Ft = 1
    j_Ft = (w_j2_ft * Ft) + b_j2_ft
    return j_Ft

def h_xt(t):
    Ft = np.sin(t * np.pi / 6)
    #Ft = 1
    x_t = (0.3 * (np.exp(-t) + 1) + 0.5 + (Ft - 10) / 100) / (b1 * np.log(b2 * (P0 + 0.5)))
    h_xt = (1 / np.sqrt(2 * np.pi * sigma ** 2)) * np.exp(-((x_t - mu) ** 2) / (2 * sigma ** 2))
    h_xt = hxt
    return h_xt

def integrate_dPn(t):
    global P1,P1a,P1b,P1c,P2,P3
    P1, _ = quad(dP1_dt, 0, t)
    P2, _ = quad(dP1_dt, 0, t)
    #P1 = dP1_dt(t)
    P1a, P1b, P1c = 0.5714 * P1, 0.1429 * P1, 0.2857 * P1
    return P1a, P1b, P1c


def dP1_dt(t):
    j1 = j1_ft(t)
    h_x = h_xt(t)
    return j1 * P1 * (1 - P1 / (h_x * K1)) * K0 + (alpha_21a * P2 + alpha_21c * P2 + alpha_31 * P3) * alpha0

def dP2_dt(t):
    j2 = j2_ft(t)
    return j2 * P2 * (1 - P2 / K2) * K0 + (alpha_1c2 * P1c + alpha_1a2 * P1a + alpha_32 * P3) * alpha0

def dP3_dt():
    return (1 - (P3 / (j3 * P1 * P2))) * P3 * K0 + (alpha_13 * P1 + alpha_23 * P2) * alpha0

def cal_P(tlen):
    global P1, P1a,P1b,P1c,P2,P3
    t_values = np.linspace(0, tlen, tlen * 10)
    dt = 0.1
    P1_list,P2_list,P3_list = [],[],[]

    for t in t_values:
        dP1 = dP1_dt(t)
        dP2 = dP2_dt(t)
        dP3 = dP3_dt()
        P1 = P1 + dP1 * dt
        P2 = P2 + dP2 * dt
        P3 = P3 + dP3 * dt
        P1_list.append(P1)
        P2_list.append(P2)
        P3_list.append(P3)

    plt.plot(t_values, P1_list, label='P1')
    plt.plot(t_values, P2_list, label='P2')
    plt.plot(t_values, P3_list, label='P3')
    # plt.plot(t_values, P3_values,label='P3')
    # plt.axhline(y=j3 * P1 * P2, color='gray', linestyle='-.', alpha=0.5)
    # 添加标题和标签
    plt.title("Simulation Result")
    plt.xlabel("Simulation Time (month)")
    plt.ylabel(r"Population $(\times 10^2)$")
    plt.legend()  # 显示图形
    plt.show()

def cal_dP(tlen):
    global P1, P1a,P1b,P1c,P2,P3
    t_values = np.linspace(0, tlen, tlen * 50)
    dt = 1 / 50
    dP1_list,dP2_list,dP3_list = [],[],[]

    for t in t_values:
        dP1 = dP1_dt(t)
        dP2 = dP2_dt(t)
        dP3 = dP3_dt()
        P1 = P1 + dP1 * dt
        P2 = P2 + dP2 * dt
        P3 = P3 + dP3 * dt
        dP1_list.append(P1)
        dP2_list.append(P2)
        dP3_list.append(P3)

    plt.plot(t_values, dP1_list, label='P1')
    plt.plot(t_values, dP2_list, label='P2')
    plt.plot(t_values, dP3_list, label='P3')
    # plt.plot(t_values, P3_values,label='P3')

    # 添加标题和标签
    plt.title("Function cal_dP1(t)")
    plt.xlabel("t")
    plt.ylabel("cal_dP1(t)")
    plt.legend()  # 显示图形
    plt.show()


# args

# 食物对七鳃鳗影响函数j1_ft
w_j1_ft = 0.1
b_j1_ft = 0.02

# 食物对本地鱼群影响函数j2_ft
w_j2_ft = 0.3
b_j2_ft = 0.18

# init P1,P2,P3 种群数量初始值

P1 = 105
P1_0 = P1
P2 = 1000
P2_0 = P2
P3 = 200
P3_0 = P3
P1a, P1b, P1c = 0.5714 * P1, 0.1429 * P1, 0.2857 * P1   # 根据时域平均分布
hxt = 0.01

# 对象之间的影响值alpha(coexisting)
alpha0 = 1e-2   # 影响力度
alpha_21a = 0.08   # 鱼群对七鳃鳗幼虫影响(+)
alpha_21c = 1   # 鱼群对七鳃鳗成虫影响(+)
alpha_31 = -1e-5   # 寄生虫对七鳃鳗的影响(-)
alpha_1c2 = -40  # 成虫对鱼群的寄生影响(-)
alpha_1a2 = 1e-19   # 幼虫对鱼群的影响甚微(+)
alpha_32 = -9e-4   # 寄50生虫对鱼群的影响 (-)
alpha_13 = 1e-6  # 七鳃鳗对寄生虫影响 (+)
alpha_23 = 1e-6  # 鱼群对寄生虫的影响 (+)
# 环境承载量
K1 = 3e3  # Carrying capacity
K2 = 3e3
K3 = 3e2
K0 = 1e-1 # 惩罚力度
j3 = K3 / (P1_0 * P2_0)


if __name__ == '__main__':
    cal_P(300)
    #print(dP3_dt())


















