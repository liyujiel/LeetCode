import collections

def groupAnagrams(strs):
    groups = collections.defaultdict(list)
    for s in strs:
        groups[tuple(sorted(s))].append(s)
    return sorted(groups.values())


import itertools

def groupAnagrams2(strs):
    groups = itertools.groupby(sorted(strs,key=sorted),sorted)
    return [sorted(members) for _, members in groups]