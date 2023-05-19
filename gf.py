def mul02(num):
    if num < 0x80:
        res = (num << 1)
    else:
        res = (num << 1) ^ 0x1b
    return res % 0x100


def mul03(num):
    return mul02(num) ^ num


def mul09(num):
    return mul02(mul02(mul02(num))) ^ num


def mul0b(num):
    return mul02(mul02(mul02(num))) ^ mul02(num) ^ num


def mul0d(num):
    return mul02(mul02(mul02(num))) ^ mul02(mul02(num)) ^ num


def mul0e(num):
    return mul02(mul02(mul02(num))) ^ mul02(mul02(num)) ^ mul02(num)
