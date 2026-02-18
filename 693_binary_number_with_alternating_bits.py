class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bin_rep=bin(n)[2:]
        flag=0
        for i in range(len(bin_rep)-1):
            if bin_rep[i]!=bin_rep[i+1]:
                continue
            else:
                flag=1
                break
        if flag==0:
            return True
        else:
            return False