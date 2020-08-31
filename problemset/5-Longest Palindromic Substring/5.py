def longestPalindrome(s: str) -> str:
    n = len(s)
    dp = []
    max_len = (0,0,0)
    for i in range(n):
        dp.append([1 if (i==j) else 0  for j in range(n)])
    #print(dp)
    
    for i in range(n-2,-1,-1):
        for j in range(i+1,n):
            if (j-i==1 and s[j]==s[i]):
                dp[i][j] = 1
                if (j-i+1>max_len[0]):
                    max_len = (j-i+1,i,j)
            elif (s[i]==s[j] and dp[i+1][j-1]):
                dp[i][j] = 1
                if (j-i+1>max_len[0]):
                    max_len = (j-i+1,i,j)
    #print(dp)
    return s[max_len[1]:max_len[2]+1]

print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))
print(longestPalindrome("ccc"))
print(longestPalindrome("aaaa"))