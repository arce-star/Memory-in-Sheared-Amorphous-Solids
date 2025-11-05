import os

def print_directory_tree(startpath, prefix=""):
    """以树形结构打印目录"""
    if prefix == "":
        print(f"{startpath}/")
    
    items = os.listdir(startpath)
    directories = [item for item in items if os.path.isdir(os.path.join(startpath, item))]
    files = [item for item in items if not os.path.isdir(os.path.join(startpath, item))]
    
    # 先打印文件
    for i, file in enumerate(files):
        if i == len(files) - 1 and not directories:
            print(prefix + "└── " + file)
        else:
            print(prefix + "├── " + file)
    
    # 再打印文件夹
    for i, directory in enumerate(directories):
        if i == len(directories) - 1:
            print(prefix + "└── " + directory + "/")
            new_prefix = prefix + "    "
        else:
            print(prefix + "├── " + directory + "/")
            new_prefix = prefix + "│   "
        
        # 递归打印子目录
        try:
            subdir_path = os.path.join(startpath, directory)
            print_directory_tree(subdir_path, new_prefix)
        except PermissionError:
            print(new_prefix + "└── [权限拒绝]")

# 打印当前目录结构
print_directory_tree('.')
