class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result=""
        min_string=min(strs,key=len)
        for i in range(0,len(min_string)):
            flag=1
            for j in range(1,len(strs)):
                if strs[0][i]!=strs[j][i]:
                    flag=0
            if flag==1:
                result+=strs[0][i]
            else:
                break
        return result