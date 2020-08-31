def three_sum(nums)->list:
    '''
    给一个nums序列，返回3个数字的序列使它们的和为0
    '''
    if len(nums) < 3:
            return []
    nums.sort()
    ans = set()
    for i,j in enumerate(nums[:-2]):
        if(i>=1 and nums[i-1]==j):
            continue
        d = dict()
        target = 0-j
        for value in nums[i+1:]:
            if d.get(value) == None:
                d[target - value] = 1
            else:
                ans.add((j,-value-j, value))
    return list(ans)


print(three_sum([-1, 0, 1, 2, -1, -4]))