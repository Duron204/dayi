# 例子1：随机验证码
# 设计一个生成随机验证码的函数，验证码由数字和英文大小写字母构成，长度可以通过参数设置。
import random
import string
ALL_CHARS = string.digits + string.ascii_letters
def generate_code(*, code_len=4):
    """
    生成指定长度的验证码
    :param code_len: 验证码的长度(默认4个字符)
    :return: 由大小写英文字母和数字构成的随机验证码字符串
    """
    return ''.join(random.choices(ALL_CHARS, k=code_len))
# 说明1：string模块的digits代表0到9的数字构成的字符串'0123456789'，string模块的ascii_letters代表大小写英文字母构成的字符串'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'。
# 说明2：random模块的sample和choices函数都可以实现随机抽样，sample实现无放回抽样，这意味着抽样取出的元素是不重复的；choices实现有放回抽样，这意味着可能会重复选中某些元素。这两个函数的第一个参数代表抽样的总体，而参数k代表样本容量，需要说明的是choices函数的参数k是一个命名关键字参数，在传参时必须指定参数名。
for _ in range(5):
    print(generate_code()) 
for _ in range(5):
    print(generate_code(code_len=6))


# 例子2：判断素数
# 设计一个判断给定的大于1的正整数是不是质数的函数。质数是只能被1和自身整除的正整数（大于1），如果一个大于1的正整数N是质数，那就意味着在2到N−1之间都没有它的因子。
def is_prime(num: int) -> bool:
    """
    判断一个正整数是不是质数
    :param num: 大于1的正整数
    :return: 如果num是质数返回True，否则返回False
    """
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True