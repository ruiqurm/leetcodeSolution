def maxSubArray_Kadane(nums: list) -> int:
    """
    Kadane算法
    dp[i] 表示以i个数结束的最大子序列的和
    dp[i] = max(dp[i-1]+nums[i],nums[i])
    """
    currentSum = cumsum = nums[0]
    for i in nums[1:]:
        currentSum = max(currentSum+i,i)
        cumsum =max(cumsum,currentSum)
    return cumsum
def maxSubArray_Kadane2(nums: list) -> int:
    """
    Kadane算法
    dp[i] 表示以i个数结束的最大子序列的和
    dp[i] = max(dp[i-1]+nums[i],nums[i])
    """
    n = len(nums)
    dp = [0]*n
    dp[0] = nums[0];
    for i,value in enumerate(nums):
        # cur = max(cur+value,i)
        if(i==0):continue
        dp[i] = max(dp[i-1]+nums[i],nums[i]);
    return max(dp)

def maxSubArray_brute_force(nums:list)->int:
    """
    蛮力.利用前缀和优化掉一个循环
    """
    n = len(nums)
    ans = -1e20
    cumsum = 0
    for i in range(n):
        partsum = cumsum
        for j in range(0,n-i):
            partsum += nums[i+j]
            ans = max(ans,partsum-cumsum)
        cumsum += nums[i]
    return ans
def maxSubArray_dp(nums:list)->list:
    """
    O(n^2)的dp，TLE
    """
    n = len(nums)
    dp =  [[0]*n for i in range(n)]
    maxx = (-1<<31)-1
    for i in range(n-1,-1,-1):
        dp[i][i] = nums[i]
        maxx = max(maxx,dp[i][i])
        for j in range(i+1,n):
            dp[i][j] = max(dp[i+1][j]+nums[i],dp[i][j-1]+nums[j])
            maxx = max(maxx,dp[i][j])
    return maxx


# print(maxSubArray_brute_force([-2,1,-3,4,-1,2,1,-5,4]))
# print(maxSubArray_dp([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray_Kadane2([-2,1]))