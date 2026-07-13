class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        resultant_array=[]
        for length in range(len(str(low)),len(str(high))+1):
            for start in range(1,11-length):
                digit=start
                number=0
                for i in range(length):
                    number=number*10+digit
                    digit+=1
                if low<=number<=high:
                    resultant_array.append(number)
        return resultant_array        
