'''
0-1 KnapSack Problem
1. Recursion
2. Memoization
3. Tabulation
4. Space Optimization

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



