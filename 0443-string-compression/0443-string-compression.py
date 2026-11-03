class Solution:
    def compress(self, chars: list[str]) -> int:
        result=""
        left=0
        count=1
        write=0
        res=[]
        max_count=0
        for right in range(1,len(chars)):
            if chars[right]==chars[left]:
                count+=1
            else:
                chars[write]=chars[left]
                write+=1
                if count>1:
                    for digit in str(count):
                        chars[write]=digit
                        write+=1
                left=right
                count=1
        chars[write] = chars[left]
        write += 1
        if count>1:
            for digit in str(count):
                chars[write]=digit
                write += 1     
        return write
