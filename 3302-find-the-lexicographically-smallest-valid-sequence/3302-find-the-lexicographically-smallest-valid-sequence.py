class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        if len(word1)<len(word2):
            return [-1]
        suffix_array=[-1]*len(word2)
        word1_index=len(word1)-1
        for word2_index in range(len(word2)-1,-1,-1):
            while word1_index>=0:
                if word1[word1_index]==word2[word2_index]:
                    suffix_array[word2_index]=word1_index
                    word1_index-=1
                    break
                word1_index-=1
        left_pointer=right_pointer=0
        result=[]
        mis_match=False
        while left_pointer<len(word1) and  right_pointer<len(word2):
            if word1[left_pointer] == word2[right_pointer]:
                result.append(left_pointer)
                left_pointer+=1
                right_pointer+=1
            else:
                if mis_match == False and (right_pointer+1 == len(word2) or suffix_array[right_pointer+1] > left_pointer):
                    result.append(left_pointer)
                    left_pointer+=1
                    right_pointer+=1
                    mis_match=True
                else:
                    left_pointer+=1
        if right_pointer==len(word2):
            return result
        return []    

        
        

        