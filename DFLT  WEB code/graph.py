import matplotlib.pyplot as plt

# 示例数据
diameters = [10, 20, 30, 40, 50]  # 直径数据
percentages = [15, 30, 45, 60, 75]  # 百分比数据

# 创建图表
plt.plot(diameters, percentages, marker='o', linestyle='-')

# 添加标题和轴标签
plt.title('Diameter vs. Percentage')
plt.xlabel('Diameter')
plt.ylabel('Percentage')

# 设置x轴刻度
plt.xticks(diameters)

# 显示网格线
plt.grid(True)

# 显示图表
plt.show()
