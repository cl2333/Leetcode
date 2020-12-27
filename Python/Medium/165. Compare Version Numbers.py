class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(i) for i in str(version1).split('.')]
        v2 = [int(i) for i in str(version2).split('.')]
        
        
        index = 0
        while index < len(v1) and index < len(v2):
            if v1[index] == v2[index]:
                index += 1 
            elif v1[index] > v2[index]:
                return 1
            else:
                return -1
        
        
        if index < len(version1) and sum(v1[index:]) != 0:
            return 1
        if index < len(version2) and sum(v2[index:]) != 0:
            return -1
        
        return 0


#neat version
def compareVersion(self, version1: str, version2: str) -> int:
	version1 = [int(pt) for pt in version1.split(".")]
	version2 = [int(pt) for pt in version2.split(".")]

	for i in range(max(len(version1), len(version2))):
		v1 = version1[i] if i < len(version1) else 0
		v2 = version2[i] if i < len(version2) else 0

		if v1 == v2:    continue
		return 1 if v1 > v2 else -1

	return 0