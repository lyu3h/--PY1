dec = 5
# 十进制转二进制
print('十进制转二进制', bin(dec))

# 十进制转八进制
print('十进制转八进制', oct(dec))

# 十进制转十六进制
print('十进制转十六进制', hex(dec))

# 二进制转十进制
dec = '110'
print('二进制转十进制', int(dec, 2))

# 八进制转十进制
dec = '12'
print('八进制转十进制', int(dec, 8))

# 十六进制转十进制
dec = 'a'
print('十六进制转十进制', int(dec, 16))

# 十六进制转二进制
dec = 'a'
print('十六进制转二进制',  bin(int(dec, 16)))

