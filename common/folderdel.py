import os

# 删除所有的文件夹和目录
def folderdel(path):
    for root, dicts, files in os.walk(path, topdown=False):
        # 删除文件
        for name in files:
            os.remove(os.path.join(root, name))
        # 删除路径
        for name in dicts:
            os.rmdir(os.path.join(root, name))

    os.rmdir(path)
