#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#注意是罗马数字转换阿拉伯数字的解法，需要理解罗马数字到阿拉伯数字的原理
#思路就是将罗马数字的最大值找出来，如果左边有字符，则减去，右边有字符，则加上
#可以尝试两位两位的计算，大在右边，则减去左边，大在左边，则加上右边，然后所有相加
#但是上面的从左往右的2位2位想家的情况，对于XIX=99不适用
#于是想到从右往左2位位相加，虽然从右往左取两位计算，但是两位以内还是满足左减右加的情况
class Solution(object):
    def romanToInt(self, s):
        rdict = {'0':0,'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        #m = -1
        sums = 0
        s = '0' + s
        for m in range(-1,-len(s),-2):
            if rdict[s[m]] > rdict[s[m-1]]:
                sums = sums + rdict[s[m]] - rdict[s[m-1]]
            else:
                sums = sums + rdict[s[m]] + rdict[s[m-1]]
            #m = m - 2
        return sums
    s = 'MCDLXXVI'
    print(romanToInt(0,s))
