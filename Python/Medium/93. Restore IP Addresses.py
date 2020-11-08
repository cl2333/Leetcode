class Solution(object):
    def restoreIpAddresses(self, s):
        def findIP(cur, s, index, result):

            if s == "" and index == 4:
                result.append(cur[:-1])
            elif index >4:
                return
            
            for i in range(1,len(s)+1):
                if i > 3:
                    break
                if s[:i] == '0' or (s[0] != '0' and 0 < int(s[:i]) < 256):
                    findIP(cur + s[:i] + '.', s[i:], index+1, result)
        
        result = []
        findIP("", s, 0, result)
        
        return result