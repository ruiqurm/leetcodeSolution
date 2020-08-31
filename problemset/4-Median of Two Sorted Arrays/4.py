def median(num1:list,num2:list)->float:
    '''
    num1,num2是有序升序列
    返回两个序列的平均值
    '''
    m,n = len(num1),len(num2)
    if m > n:
        # 保证m>n
        num1,num2 = num2,num1
        m,n = n,m
    
    
    median_pos = (m + n + 1)  //2 
    imin = 0
    imax = m

    #二分查找
    while(imin<=imax):
        i = (imin+imax) // 2
        j = median_pos  - i 
        if (i<m and num2[j-1]>num1[i]):
            imin = i + 1
        elif (i>0 and num1[i-1]>num2[j]):
            imax = i - 1
        else:
            # 正好 
            # 考虑几个边界条件
            if i==0:
                left_max = num2[j-1]
            elif (j==0):
                left_max = num1[i-1]
            else:
                left_max = max(num2[j-1],num1[i-1])
            if (n+m)%2==1:
                return left_max
            if i==m:
                right_min = num2[j]
            elif j == n:
                right_min = num1[i]
            else:
                right_min = min(num1[i],num2[j])
            return (right_min+left_max) / 2.0

print(median([1,3],[2]))
