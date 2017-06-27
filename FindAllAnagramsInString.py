from collections import Counter

def findAnagrams(self,s,p):
    '''
    :type s: str
    :type p:str
    :rtype: List[int]
    '''
    res = []
    pCounter = Counter(p)
    sCounter = Counter(s[:len(p)-1])
    for i in range(len(p)-1,len(s)):
        sCounter[s[i]] += 1 # include a new char in the window
        if sCounter == pCounter: # this step is O(1) since there are at most 26 English Letters 
            res.append(i-len(p)+1) # append starting index
        sCounter[s[i-len(p)+1]] -= 1 #decrease the count of the oldest char in the window 
        if sCounter[s[i-len(p)+1]] == 0:
            del sCounter[s[i-len(p)+1]]
    return res
    
