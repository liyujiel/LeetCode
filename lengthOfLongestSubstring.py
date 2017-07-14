def lenthOfLongestSubstring(s):
    ans, left, last = 0, 0, {}
    for i in range(len(s)):
        if s[i] in last and last[s[i]] >= left:
            left = last[s[i]] + 1
        last[s[i]] = i
        ans = max(ans, i - left + 1)
    return ans