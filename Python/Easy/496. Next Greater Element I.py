class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for i in nums1:
            j=nums2.index(i)
            
            flag=True
            for k in nums2[j:]:
                if k > i:
                    ans.append(k)
                    flag=False
                    break
            if flag:        
                ans.append(-1)
                
        return ans

        #simpler version
        return [next((y for y in nums[nums.index(x):] if y > x), -1) for x in findNums]

    #using stack
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        s = []
        ans = []
        
        for i in nums2:
            while s and s[-1] < i:
                d[s.pop()]=i
            s.append(i)
            
        return [d.get(i,-1) for i in nums1]
