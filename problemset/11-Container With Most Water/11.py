def maxArea(height:list) -> int:
    """
    
    """
    i, j = 0, len(height)-1
    max_area = -1
    while(i!=j):
        max_area = max(max_area,min(height[i],height[j])*(j-i) )
        if(height[i]<height[j]):
            i+=1
        else:
            j-=1
        if(height[i]==height[j] and (i-j)>2):
            i+=1
    return max_area

print(maxArea([1,8,6,2,5,4,8,3,7]))
            

        