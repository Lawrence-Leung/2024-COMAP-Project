import scipy.stats as stats
import csv

# 打开CSV文件
with open('layer1.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    headers = next(csvreader)  # 如果有标题行，读取标题行

    # 初始化一个字典来保存每列的数据，每个键对应列的标题
    columns = {header: [] for header in headers}

    # 读取CSV文件的每一行
    for row in csvreader:
        for header, value in zip(headers, row):
            columns[header].append(value)

# 现在 columns 字典包含了每一列的数据
# 例如，获取第一列的数据
list1 = columns[headers[0]]
list2 = columns[headers[1]]
list3 = columns[headers[2]]
list4 = columns[headers[3]]
list5 = columns[headers[4]]



# 你可以使用嵌套循环来计算所有可能的两两组合的Kendall秩相关系数
data_sets = [list1,list2,list3,list4,list5]

for i in range(len(data_sets)):
    for j in range(i+1, len(data_sets)):
        tau, p_value = stats.kendalltau(data_sets[i], data_sets[j])
        print(f"Kendall's tau between data set {i+1} and {j+1}: {tau:.3f}, p-value: {p_value:.3f}")
