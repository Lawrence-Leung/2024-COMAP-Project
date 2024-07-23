
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
b = -34.16
c = 400

# 确保a不
solutions = solve_quadratic_equation(a, b, c)

print(f"x1 = {solutions[0]}")
print(f"x2 = {solutions[1]}")