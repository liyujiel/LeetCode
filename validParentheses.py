def isValid(self,s):
    validDict = {")":"(","]":"[","}":"{"}
    stack = []
    for breket in s:
        if breket in validDict.values():
            stack.append(breket)
        elif breket in validDict.keys():
            if stack == [] or validDict[breket] != stack.pop():
                return False
        else:
            return False
    return len(stack)==0
            