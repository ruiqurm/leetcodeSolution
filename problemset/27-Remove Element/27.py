def removeElement(nums: list, val: int) -> int:
    index = 0
    while(index<len(nums)):
        if(nums[index]==val):
            del nums[index]
        else:
            index+=1
    return len(nums)

print(removeElement([0,1,2,2,3,0,4,2],2))