convertString='0123456789ABCDEF'
def convert(num,jinzhi=16):
    if num//jinzhi==0:
        return convertString[num]
    else:
        return convert(num//jinzhi,jinzhi)+convertString[num%jinzhi]

print(convert(160))