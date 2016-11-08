#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Solution(object):
    def twoSum(self, nums, target):
        t_nums = set([target - x for x in nums])
        o_nums = set(nums)
        r_nums = list(t_nums & o_nums)#取并集之后的list
        result = []
        for n in range(len(nums)-1):
            if nums[n] == r_nums[0] or nums[n] == r_nums[1]:
                result.append(n)
        return result
    h = twoSum(9,[2,11,7,15],9)
    print(h)












