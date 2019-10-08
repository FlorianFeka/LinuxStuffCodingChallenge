# This problem was asked by Amazon.

# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

def longestSubstring(s, k):
    longestSubstring = ''
    for i in range(len(s)):
        for j in range(i, len(s)):
            currentSubstring = s[i:j]
            if(len(longestSubstring) < len(currentSubstring) and len(set(currentSubstring)) <= k):
                longestSubstring = currentSubstring
    return longestSubstring

print(longestSubstring("abcba", 2))