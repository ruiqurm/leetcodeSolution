def removeDuplicates(nums:list) -> int:
    '''

    '''

    if (len(nums)==1):return 
    last,now = 0,1

    while(now<len(nums)):
        if(nums[now] == nums[last]):
            del nums[now]
        else:
            last = now
            now += 1
    return len(nums)

print(removeDuplicates([1,1,2]))
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))