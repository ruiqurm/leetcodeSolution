def longestPalindromeSubseq(s: str) -> int:
    n = len(s)
    dp =  [[0]*n for i in range(n)]
    for i in range(n-1,-1,-1):
        for j in range(i,n):
            if (i==j):
                dp[i][j] = 1
            elif (i+1==j and s[i]==s[j]):
                dp[i][j] = 2
            elif(s[i]==s[j]):
                dp[i][j] = dp[i+1][j-1]+2
            else:
                dp[i][j] = max(dp[i+1][j],dp[i][j-1])
    else:return dp[0][n-1]

print(longestPalindromeSubseq("bbbab"))
print(longestPalindromeSubseq("abcdef"))
print(longestPalindromeSubseq("abcabcabcabc"))