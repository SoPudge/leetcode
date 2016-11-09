#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#第一种解法
#第一种解法是穷举法，核心在于两个循环
#第一个循环专门用于循环nums当中值的下标，从0开始，所以range没有第一个参数
#第二个循环专门用于循环nums当中值的下标，也从0开始
#就是nums当中第一个值，和nums当中所有的值对比，是否为target，第二个值对比所有，第三个对比所有
#有一种情况是，m = n，意义就是特殊情况下，判断4+4=8这种情况，那就是自身和自身相加，就等于target了
class Solution(object):
    def twoSum(self, nums, target):
        for m in range(len(nums)):
            for n in range(len(nums)):
                if nums[m] == target - nums[n] and m != n:
                    return [m,n]
    h = [2,6,12,7,8]
    m = 9
    print(twoSum(0,h,m))
#第二种解法
#第二种解法通过字典的形式加快计算速度，核心意义在于
#将nums通过enumerate分解为kv字典，其中k是下标，v是值，这样就知道每个值对应的下标是多少
#在构造一个target-v的字典，其中key为target-v，value为k，通过引用dicr[target-v]就知道对应的key是多少
#这样的话，通过if判断nums当中的v是否在dicr中，如果在的话，那么显然dicr当中对应的k值，加上nums当中的k值就是target了
#注意nums当中的kv是正向的，而dicr当中的kv是反向的，v是下标，k是值，这样方便dicr来引用直接获得k的值
class Solution(object):
    def twoSum(self, nums, target):
        dicr={}
        for k,v in enumerate(nums):
            if v in dicr:
                return [dicr[v],k]
            else:
                dicr[target - v] = k
    h = [2,6,12,7,8]
    m = 9
    print(twoSum(0,h,m))

#总结，第二种方法的好处是，通过dict大大加快了循环遍历的速度，巧妙地通过kv值互换，利用到dict[k] = v这个特性
