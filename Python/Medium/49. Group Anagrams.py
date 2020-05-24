from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = []
        mappings={}
        count = 0
        
        for str in strs:
            mapping = Counter(str)
            # mapping = {}
            # for i in str:
            #     if i not in mapping:
            #         mapping[i] = 1
            #     else:
            #         mapping[i] += 1
            
            if mapping not in mappings.values():
                mappings[count] = mapping
                results.append([str])
                count += 1
            else:
                for key, value in mappings.items():
                    if mapping == value:
                        results[key].append(str)
        
        return results
                

#simpler version
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        output_dict = {}

        for s in strs:
            string = ''.join(sorted(s)) 

            if string in output_dict:
                output_dict[string].append(s)
            else:
                output_dict[string] = [s]

        return list(output_dict.values())