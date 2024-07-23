import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


# Define the model
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
    plt.plot(t, P_nmal, label='Population P(t)')
    plt.title('Population over Time')
    plt.xlabel('Time t')
    plt.ylabel('Population P(t)')
    plt.legend()
    plt.grid(True)
    plt.show()


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
T = 120  # Time span for simulation

# 用于反馈调节的东西
b1 = 0.5
b2 = 800
#x_t = 0.5

# This is just a demonstration, the user should use their own values for the parameters
simulate_population(K, mu, sigma, a1, a2, P0, T, b1, b2) # Uncomment this line to run the simulation with the example values

# The simulate_population function is the interface that can be used to adjust parameters and observe the effect.
# The user can call this function with different values to run their own simulation.
