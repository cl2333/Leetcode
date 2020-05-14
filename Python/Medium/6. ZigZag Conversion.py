class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result = ""
        for i in range(numRows):
            row = []
            index = i
            count = 0
            while index < len(s):
                if  i == 0 or i == numRows -1:
                    row.append(s[index])
                    index += 2*numRows - 2
                else:
                    if count % 2 == 0:
                        row.append(s[index])
                        index += 2*numRows - 2*(i+1)
                        count += 1
                    else:
                        row.append(s[index])
                        index += 2*i
                        count += 1
            print(row)
            result += "".join(row)
            count = 0
        return result
                
        
#better solution
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        lin = 0
        pl = 1
        outp = [""] * numRows
        for i in range(len(s)):
            outp[lin] += s[i]
            if numRows > 1:
                lin += pl
                if lin == 0 or lin == numRows -1:
                    pl *= -1
        outputStr = ""
        for j in range(numRows):
            outputStr += outp[j]
        return outputStr