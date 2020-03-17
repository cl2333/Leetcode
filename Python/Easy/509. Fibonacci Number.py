class Solution:
    def fib(self, N: int) -> int:
        n=[0, 1]
        if N<=1:
            return n[N]
        
        for i in range(2,N+1):
            n.append(n[i-1]+n[i-2])
        
        return n[N]

        #using recurssive
        if N < 2: 
            return N
        return self.fib(N-1) + self.fib(N-2)