def convert(x, base):
    alphabet = '0123456789ABCDEF'
    res = ''
    while x > 0:
        res += alphabet[x % base]
        x //= base
    return res[::-1]


def some():
    count = 0
    for i in range(10, 18):
        count += convert(i, 5).count('2')
    print(count)


def reshu_ege_7761():
    print(bin(4 ** 2020 + 2 ** 2017 - 15)[2:].count('1'))


# reshu_ege_7761()

def reshu_ege_2302():
    base = 1
    while True:
        base += 1
        if convert(18, base) == '30':
            print(base)
            break


# reshu_ege_2302()

def pol_4886():
    res = convert(8 ** 888 + 16 ** 1617 - 2 ** 444, 8)
    max_digit = max(list(res))
    print(res.count(max_digit))


# pol_4886()

def pol_4416():
    res = convert(16 ** 44 * 16 ** 30 - (32 ** 5 * (8 ** 40 - 8 ** 32) * (16 ** 17 - 32 ** 4)), 16)
    res = res.replace('E', '1')
    res = res[:-5] + res[-4:]
    print(res.count('1'))


# pol_4416()

# res = '123456789'
# print(res[:-3] + res[-2:])
