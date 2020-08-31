#from array import array
def two_sum(nums:list,target:int)->int:
    d = dict()
    for index,value in enumerate(nums):
        remain = target - value
        if (remain in d and d[remain]!=index):
            # 找到了
            return [d[remain],index]
        d[value] = index
    return []

# 更简洁、更快的写法：
def two_sum_2(nums,target)->int:
    d = dict()
    for index,value in enumerate(nums):
        if d.get(value) == None:
            d[target - value] = index
        else:
            return [d.get(value), index]
print(two_sum(nums = [-3,4,3,90], target = 0))
            