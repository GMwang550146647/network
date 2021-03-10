'''近似完美散列函数：'''
import hashlib
'''1.MD5'''
hash1=hashlib.md5("hello world!").hexdigest()
print(hash1)
'''
2.SHA系列函数:
sha1:160位
sha224：224位
sha256：256位
sha384：384位
sha512: 512位
'''
hash2=hashlib.sha1("hello world!").hexdigest()
print(hash2)
