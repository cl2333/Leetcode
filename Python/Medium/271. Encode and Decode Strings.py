class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        result = ""
        for s in strs:
            result += str(len(s))
            result += " "
            result += s
            
        return result


    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        if not s:
            return []
        
        i, start, length = 0, 0, 0
        result = []
        while i < len(s):
            if s[i] != " ":
                length = length * 10 + int(s[i])
                i += 1
            elif s[i] == " ":
                i += 1
                result.append(s[i:i + length])
                i += length
                length = 0
                
        
        return result
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))