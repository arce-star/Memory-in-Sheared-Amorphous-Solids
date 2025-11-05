import os

# 查看当前目录结构
print("当前目录内容:")
for item in os.listdir('.'):
    if os.path.isdir(item):
        print(f"文件夹: {item}")
        for file in os.listdir(item):
            print(f"  - {file}")
