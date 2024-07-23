import csv

# 创建空列表
location2, location3, location4, location5, location6, location8 = ([] for _ in range(6))

# 读取CSV文件
csv_file_path = 'data.csv'  # 请将 'data.csv' 替换为您的CSV文件路径

with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # 假设B, D, E列的标题分别是'B', 'D', 'E'
        b_value = int(row['B'])
        d_value = row['D']
        e_value = row['E']
        de_tuple = (d_value, e_value)

        # 根据B列的值，将D列和E列的值封装成元组并存放到对应的列表中
        if b_value == 2:
            location2.append(de_tuple)
        elif b_value == 3:
            location3.append(de_tuple)
        elif b_value == 4:
            location4.append(de_tuple)
        elif b_value == 5:
            location5.append(de_tuple)
        elif b_value == 6:
            location6.append(de_tuple)
        elif b_value == 8:
            location8.append(de_tuple)



def cal_sex_ratio_sep_year(data_list):
    # 使用字典来存储每一年的数据
    years_data = {str(year): [] for year in range(6)}

    # 分类数据到对应年份
    for i in data_list:
        year_key = i[0]
        if year_key in years_data:
            years_data[year_key].append(i[1])

    # 计算性别比例
    years_ratio = {}
    for year, sexes in years_data.items():
        m_num = sexes.count('1')
        f_num = sexes.count('0')
        # 避免除以零的错误
        years_ratio[year] = 'N/A' if m_num == 0 else str(m_num / (m_num + f_num)) +' cal_num='+ str(m_num + f_num)

    # 打印每年的性别比例
    for year, ratio in years_ratio.items():
        print(f'year{year}: {ratio}')

def cal_sex_ratio_total(data_list):
    sexes = []
    for a in data_list:
        sexes.append(a[1])

    m_num = sexes.count('1')
    f_num = sexes.count('0')
    # 避免除以零的错误
    total_ratio = 'N/A' if m_num == 0 else m_num / (m_num + f_num)
    tol_num = m_num + f_num
    name = get_variable_name(data_list)
    print(name,'total ratio: ', total_ratio, ' cal_num=' ,tol_num)

def get_variable_name(variable):
    for name, value in globals().items():
        if id(value) == id(variable):
            return name

if __name__ == '__main__':
    for r in [location2,location3,location4,location5,location6,location8]:
        cal_sex_ratio_total(r)
        cal_sex_ratio_sep_year(r)
        print('\n\n')

    print('Cal the total data ratio...\n')
    total_data = location2 + location3 + location4 + location5 + location6 + location8
    cal_sex_ratio_total(total_data)
    cal_sex_ratio_sep_year(total_data)
    print('\nDone.')
