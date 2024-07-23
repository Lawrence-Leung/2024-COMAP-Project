import matplotlib.pyplot as plt

def plot_point(p1,p2):


    # 创建散点图
    x,y = [p1[0],p2[0]], [p1[1],p2[1]]
    plt.figure(figsize=(3,3))
    plt.scatter(x,y, marker='x', color='red', s=100)  # s是标记的大小

    # 设置图表标题和坐标轴标签

    plt.title('Pole distribution diagram')
    plt.xlabel('Real axis')
    plt.ylabel('Imaginary axis')

    # 确定坐标轴的范围
    x_range = max(x) - min(x)
    y_range = max(y) - min(y)
    offset = max(x_range, y_range)

    plt.xlim(-offset, offset)
    plt.ylim(-offset, offset)

    # 在(0,0)处画一条垂直线和一条水平线
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)

    # 显示图表
    plt.show()

# 定义点
p1 = [17.075647321060842,10.36930212825744]
p2 = [17.075647321060842,-10.36930212825744]
# 调用函数绘制散点图
plot_point(p1,p2)
