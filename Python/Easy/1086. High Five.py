class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        
        highFive = {}
        
        for i in range(len(items)):
            if items[i][0] in highFive:
                highFive[items[i][0]].append(items[i][1])
            else:
                highFive[items[i][0]]=[items[i][1]]
           
        output = []
        
        for i in highFive.keys():
            if len(highFive[i]) <=5:
                output.append([i,int(sum(highFive[i])/len(highFive[i]))])
            else:
                output.append([i,int(sum(sorted(highFive[i],reverse=True)[:5])/5)])

        sorted(output)
        
        return output
                
# simpler version
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        d={}
        for i in items:
            try:
                d[i[0]].append(i[1])
            except:
                d[i[0]]=[i[1]]
        for i in d:
            d[i].sort()
            d[i]=d[i][::-1][:5]
        return [[i,sum(d[i])//len(d[i])] for i in d]