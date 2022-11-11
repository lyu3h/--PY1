import random
import string

all_chs=string.digits+string.ascii_letters     #包含0-9+a-z+A-Z的字符 一共62个字符


def gen_pass(n=8):
    result=''
    for i in range(n):
        ch=random.choice(all_chs)                #从all_chs中选择一个字符
        result+=ch                                          #拼接
    return result

print(gen_pass())                                        #输出8个随机字符
