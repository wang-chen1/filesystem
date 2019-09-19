import os

# 遍历文件夹和目录
def traversal(bool, path):
    # path = '/home/xh/filesystem/media'
    dicts_ = []
    files_ = []
    # 遍历所有文件和文件夹的路径
    if bool is True:
        for root, dicts, files in os.walk(path):
            for name in dicts:
                # print(name)
                dicts_.append(os.path.join(root, name))
            for name in files:
                # print(name)
                files_.append(os.path.join(root, name))
        # print(dicts_, 10 * '-', files_)
        return dicts_, files_
    # 只遍历同级,且只取文件名和文件夹名
    elif bool is False:
        for root, dicts, files in os.walk(path):
            if root != path:
                break
            for name in dicts:
                # print(name)
                dicts_.append(name)
            for name in files:
                files_.append(name)
        return dicts_, files_

# traversal(bool=True,
#           path='/home/xh/filesystem/media/www/我的文件/其他/qqq')
