class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreater = [-1] * len (nums1)
        stack = []
        for i in range (len(nums2)):
                while stack and stack[-1] < nums2[i]:
                    a = stack[-1]
                    stack.pop()
                    nextGreater[nums1.index(a)] = nums2[i]
                if nums2[i] in nums1 and ( stack == [] or stack[-1] > nums2[i] ) :      
                    stack.append(nums2[i]) 
        return nextGreater
                
        
