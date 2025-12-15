"""
Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "zxyzxyz"

Output: 3

Explanation: The string "xyz" is the longest without duplicate characters.

Example 2:

Input: s = "xxxx"

Output: 1

Constraints:

    0 <= s.length <= 1000
    s may consist of printable ASCII characters.

pseudocode
intialize start pointer at left = 0
initialize hash map for word: frequency value pair
initialize the length of current longest string
loop through s
increment the frequency of the specific char

if the char frequency > 1:
decrease the frequency by 1
start += 1

update the length

return the longest string length

"""
def lengthOfLongestSubstring(s):
    start = 0
    tbl = {}
    maxlength = 0

    for i in range(len(s)):
        tbl[s[i]] = 1 + tbl.get(s[i], 0)

        while tbl[s[i]] > 1:
            # 2. so we have to remove the frequency of start by 1, squeeze the window
            tbl[s[start]] -= 1

            # 1. we progress, move start to right by 1
            start += 1

        maxlength = max(maxlength, i - start + 1)

    return maxlength

if __name__ == "__main__":
    print(lengthOfLongestSubstring("xxxx"))

