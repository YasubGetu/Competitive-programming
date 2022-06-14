class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = defaultdict (int)
        sum = 0
        incremented = 0
        counter = []
        for nums in arr:
            count [nums] += 1
        for val in count.values():
            counter.append(val) 
        counter.sort()
        for i in range (len(counter)-1 , -1 , -1):
            sum += counter[i] 
            incremented += 1
            if sum >= int(len(arr)/2):
                return incremented
