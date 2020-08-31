def threeSumClosest(nums: list, target: int) -> int:
    nums.sort()
    len_nums = len(nums)
    if(len_nums<=3):
        return sum(nums)
    diff,diff_value = 1e5,0
    for index,value in enumerate(nums[:-2]):
        front,tail = index+1,len_nums-1
        while(front!=tail):
            new_sum = value+nums[front]+nums[tail]
            new_diff = abs(new_sum-target)

            #diff = min(new_diff,diff)
            if new_diff<diff:
                diff = new_diff
                diff_value = new_sum
            if new_sum<target:
                front+=1
            else:
                tail-=1
    return diff_value

print(threeSumClosest([-1,2,1,-4],1))

                
