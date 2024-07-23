import matplotlib.pyplot as plt


# 定义归一化函数
def normalize(data):
    min_val = min(data)
    max_val = max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]


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
# 创建一个新的图形窗口
plt.figure(figsize=(15, 10))  # 可以通过figsize调整整个画布的大小

# 定义子图行列数
rows = 2
cols = 3


# 绘制每个湖的散点图
lakes = [('Superior', Superior_norm), ('Michigan', Michigan_norm),
         ('Huron', Huron_norm), ('Erie', Erie_norm),
         ('Ontario', Ontario_norm), ('small_lake', small_lake_norm)]



for i, (lake_name, lake_data) in enumerate(lakes):
    plt.subplot(rows, cols, i + 1)  # 创建子图
    plt.scatter(years, lake_data)

    # 添加标题
    plt.title(f'Normalized {lake_name} Measurements')
    plt.xticks(years)
    # 添加轴标签
    plt.xlabel('Measurement Number')
    plt.ylabel('Normalized Value')

# 调整子图间距
plt.tight_layout()

# 显示图表
plt.show()