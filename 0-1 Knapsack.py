'''
0-1 KnapSack Problem
1. Recursion
2. Memoization
3. Tabulation
4. Space optimization

Input: W = 4, val[] = {1,2,3}, wt[] = {4,5,1}
Output: 3
Explanation: Choose the last item that weighs 1 unit and holds a value of 3. 

'''

#recursion
def knapSack(self,W, wt, val):
        def f(i,w,wt,val):
            if i==0:
                if wt[0]<=w: #if wt[0] can still fit in bag take it
                    return val[0]
                return 0 #dont take if no space
            nottake = 0 + f(i-1,w,wt,val) #dont take current item, move to next
            take = -1e7
            if wt[i]<=w: #if item taken can fit, take its value
                take = val[i] + f(i-1,w-wt[i],wt,val) #reduce in bag before moving to nxt
            return max(take, nottake)        
        
        n = len(wt)
        return f(n-1,W,wt,val)

#memoization
def knapSack(self,W, wt, val):
        def f(i,w,wt,val,dp):
            if i==0:
                if wt[0]<=w: #if wt[0] can still fit in bag take it
                    return val[0]
                return 0 #dont take if no space
                
            if dp[i][w]!=-1:
                return dp[i][w]
                
            nottake = 0 + f(i-1,w,wt,val,dp) #dont take current item, move to next
            take = -1e7
            if wt[i]<=w: #if item taken can fit, take its value
                take = val[i] + f(i-1,w-wt[i],wt,val,dp) #reduce in bag before moving to nxt
            dp[i][w] = max(take, nottake) 
            return dp[i][w]
        
        n = len(wt)
        dp = [[-1 for j in range(W+1)] for i in range(n)]
        return f(n-1,W,wt,val,dp) 

#tabulation
def knapSack(self,W, wt, val):
        n = len(wt)
        dp = [[0 for j in range(W+1)] for i in range(n)]
        for w in range(wt[0],W+1):
            dp[0][w] = val[0]
        
        for i in range(1,n):
            for w in range(W+1):
                nottake = 0 + dp[i-1][w] #dont take current item, move to next
                take = -1e7
                if wt[i]<=w: #if item taken can fit, take its value
                    take = val[i] + dp[i-1][w-wt[i]] #reduce in bag before moving to nxt
                dp[i][w] = max(take, nottake)
        return dp[n-1][W]


#space optimization
def knapSack(self,W, wt, val):
        n = len(wt)
        prev = [0]*(W+1)
        curr = [0 for j in range(W+1)]
        for w in range(wt[0],W+1):
            prev[w] = val[0]
        
        for i in range(1,n):
            for w in range(W+1):
                nottake = 0 + prev[w] #dont take current item, move to next
                take = -1e7
                if wt[i]<=w: #if item taken can fit, take its value
                    take = val[i] + prev[w-wt[i]] #reduce in bag before moving to nxt
                curr[w] = max(take, nottake)
            prev=curr[:]
        return prev[W]
        



