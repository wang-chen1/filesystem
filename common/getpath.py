import os

# 获取路径
def getpath(*args):
    path = os.getcwd()
    for arg in args:
        path = os.path.join(path, arg)
    return path


# if __name__ == '__main__':
#     getpath()
