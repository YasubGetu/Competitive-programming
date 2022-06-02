class Solution:
    def sortSentence(self, s: str) -> str:
        x = s.split()
        dict = {}
        answer = ""
        for i in range(len(x)):
            last = int(x[i][-1])
           
            dict [last] = x[i][:len(x[i]) - 1]
        for i in range (len(x)):
            answer = answer + dict [i+1] + " "
        answer = answer[: len(answer)-1]    
        return answer    
            
