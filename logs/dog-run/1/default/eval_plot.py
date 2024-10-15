import matplotlib.pyplot as plt
import csv
import os

# CSV 文件路径
csv_file_path = 'eval.csv'

# 检查文件是否存在
if not os.path.exists(csv_file_path):
    print(f"文件 {csv_file_path} 不存在。请检查文件路径。")
    exit(1)

# 初始化数据列表
steps = []
rewards = []

# 读取 CSV 文件
with open(csv_file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # 跳过标题行
    for row in csvreader:
        steps.append(float(row[0]))
        rewards.append(float(row[1]))

# 检查数据是否正确读取
if not steps or not rewards:
    print("未能正确读取数据，请检查 CSV 文件内容。")
    exit(1)

# 绘制图表
plt.figure(figsize=(10, 6))
plt.plot(steps, rewards, marker='o', linestyle='-', color='b')
plt.xlabel('Step')
plt.ylabel('Episode Reward')
plt.title('Episode Reward vs Step')
plt.grid(True)
plt.show()
print("图表绘制完成。")