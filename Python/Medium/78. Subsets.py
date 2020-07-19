class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.get_result([[]], nums, [[]])
        
    def get_result(self, begin, left, result):
        if left == []:
            return result

        for i in range(len(left)):
            num = left[i]
            last = begin[-1].copy()
            last.append(num)
            result.append(last)
            begin.append(last)
            self.get_result(begin, left[i+1:], result)
            begin.pop()
            
        return result


#simpler version
def subsets(self, nums: List[int]) -> List[List[int]]:
        m=[]
        self.sub(nums,0,m,[])
        return m
def sub(self,nums,ind,m,t):
	m.append(list(t))
	for i in range(ind,len(nums)):
		t.append(nums[i])
		self.sub(nums,i+1,m,t)
		t.pop()