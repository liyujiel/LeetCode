import collections

def groupAnagrams(strs):
    groups = collections.defaultdict(list)
    for s in strs:
        groups[tuple(sorted(s))].append(s)
    return sorted(groups.values())