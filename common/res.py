def res(code=0, msg='SUCCESS', action='', data=[]):
    r = {
        'code': code,
        'msg': msg,
        'action': action,
        'data': data,
    }
    return r


if __name__ == '__main__':
    data = res(code=1, msg='hello')
    print(data)
