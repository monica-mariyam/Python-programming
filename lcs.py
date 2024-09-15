'''
LCS - Longest Common Subsequence
1. Recursion
2. Memoization
3. Tabulation
'''

#recursion
def f(ind1, ind2, str1, str2):
            if ind1<0 or ind2<0:
                return 0
            if str1[ind1]==str2[ind2]:
                return 1+f(ind1-1,ind2-1,str1,str2)
            return max(f(ind1-1,ind2,str1,str2), f(ind1,ind2-1,str1,str2))
        return f(n-1,m-1,str1,str2)

#memoization
def lcs(self, n, m, str1, str2):
        def f(ind1, ind2, str1, str2, dp):
            if ind1<0 or ind2<0:
                return 0
            if dp[ind1][ind2]!=-1:
                return dp[ind1][ind2]
            if str1[ind1]==str2[ind2]:
                return 1+f(ind1-1,ind2-1,str1,str2,dp)
            dp[ind1][ind2] = max(f(ind1-1,ind2,str1,str2,dp), f(ind1,ind2-1,str1,str2,dp))
            return dp[ind1][ind2]
        
        dp = [[-1 for j in range(m)] for i in range(n)]
        return f(n-1,m-1,str1,str2,dp)

#tabulation
def lcs(self, n, m, str1, str2):
        dp = [[-1 for j in range(m+1)] for i in range(n+1)]
        #shifting the indices
        for i in range(n+1):
            dp[i][0] = 0
        for j in range(m+1):
            dp[0][j] = 0
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                if str1[i-1]==str2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
       
        return dp[n][m]

#space optimization
 def lcs(self, n, m, str1, str2):
        prev = [0]*(m+1)
        curr = [0]*(m+1)
        for i in range(1,n+1):
            for j in range(1,m+1):
                if str1[i-1]==str2[j-1]:
                    curr[j] = 1+prev[j-1]
                else:
                    curr[j] = max(prev[j], curr[j-1])
            prev=curr[:]
       
        return prev[m]
