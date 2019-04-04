#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Int16  相当于 short  占2个字节   -32768 ~ 32767


def intToBin32(i):
    return (bin(((1 << 32) - 1) & i)[2:]).zfill(32)

def intToBin16str( i):
    """ int TO str """
    print(i)
    return (bin(((1 << 16) - 1) & i)[2:]).zfill(16)

def bin16strToInt( s):
    """ str TO int """
    print(s)
    print(type(s))
    return int(s[1:], 2) - int(s[0]) * (1 << 15)

def hexTo16int(j):
    """ hex 如 0x8543 转为int类型 """
    ddd = 0x8000
    i = j
    if (j&ddd == 0):
        print(" 大于零")
        # 补码等于原码
        # 符号位为零
        ii = i
        #补码->原码
        iii = ii
        # 赋予符号
        return iii * 1
    else:
        print("小于零")
        ii = i
        #补码->反码
        # 补码等于反码加一
        iii = ii - 1
        #反码->原码
        iiii = ~iii
        iiii = iiii & 0x7fff # 消除符号位
        # 赋予符号
        return iiii * -1

    

if __name__ == "__main__":

    # 7  0x7   -7  0xfff9
    result_m = hexTo16int(38964)
    print(result_m)



# 验证 bin16strToInt()   intToBin16str()
    imin = -0x7fff-1
    imax = 0x7fff
    for i in range(imin, imax+1):
        print(i)
        i = 0x7777  #fftest
        str_i = intToBin16str(i)
        print(type(str_i))
        if i != bin16strToInt(intToBin16str(i)):
            print(i, "x") # 没有输出，说明转换是正确的
