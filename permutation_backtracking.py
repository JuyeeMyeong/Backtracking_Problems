class Solution:
    def permute(self, nums):
        # check validation [1, 2, 3] if number is in the list,
        # skip, or put in in the list for i in N
        # backtrack 
        self.nums = nums
        self.result = []
        if not self.nums:
            return self.result
        self.backtrack_permute([])
        return self.result
    
    def backtrack_permute(self, possible):
        if len(possible) == len(self.nums):
            self.result.append(possible.copy())
            return
        for i in range(len(self.nums)):
            if self.nums[i] not in possible:
                possible.append(self.nums[i])
                self.backtrack_permute(possible)
                possible.pop()
        
