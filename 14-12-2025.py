"""
3. Longest Substring Without Repeating Characters
Medium
Topics
premium lock iconCompanies
Hint

Given a string s, find the length of the longest without duplicate characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.

"""

def lengthOfLongestSubstring(s):
    # initialize window
    start = 0

    # initialize result to keep track current longest string length
    res = 0

    # initialize a dict to store: {char: freq} pairs
    tbl = {}

    # loop through the string s
    for i in range(len(s)):
        # add every char into a dict
        tbl[s[i]] = 1 + tbl.get(s[i], 0)

        while tbl[s[i]] > 1:
            tbl[s[start]] -= 1
            start += 1

        res = max(res, i - start + 1)

    return res
    

if __name__ == "__main__":
    print(lengthOfLongestSubstring("pwwkew"))