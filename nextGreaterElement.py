class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreater = []
        for i in range (len(nums1)):
            holder = nums2.index(nums1[i])
            for j in range(holder + 1 , len(nums2) , 1):
                if nums2[holder] < nums2[j]:
                    nextGreater.append(nums2[j])
                    break        
            if len(nextGreater) < i + 1:
                nextGreater.append(-1)
        return nextGreater                     
        
