def trans(string: str):
    """
    将字符串去掉'_',首字母大写，然后重新拼接
    :param string:
    :return: string
    """
    res = ''
    list_string = string.split('_')
    for i in list_string:
        res += i.capitalize()
    return res


if __name__ == '__main__':
    source = 'Multi-Domain Subsystem'
    print(trans(source))
