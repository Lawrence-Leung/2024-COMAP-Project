from scipy.stats import norm

# 生成随机样本
for i in range(15):
    Gaussion_Sample = norm(loc=1, scale=0.0752).rvs()
    print(Gaussion_Sample)
    print(i)

