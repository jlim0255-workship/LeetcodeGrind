"""
Longest Repeating Character Replacement

You are given a string s consisting of only uppercase english characters and an integer k. 
You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

Example 1:

Input: s = "XYYX", k = 2

Output: 4

Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

Example 2:

Input: s = "AAABABB", k = 1

Output: 5

Constraints:

    1 <= s.length <= 1000
    0 <= k <= s.length



pseudocode
use slidng window

initialize start = 0
initialize hash map
initialize longest length to hold char: frequency pairs

loop through list s
increase the frequency in the hashmap

while s[start] != s[i] and tbl[s[i]] > k:  (wrong)

(this is how much extra steps i needed)
while length - most frequent value in hash map > k
# shrink the window
s[start] -= 1
start += 1

calculate the current max

return final res
"""
def characterReplacement(s, k):
    # make string a list
    lst = [char for char in s]

    # initialize start
    start = 0

    # initialize hash map
    tbl = {}

    # initialize current length
    maxlength = 0

    for i in range(len(lst)):
        tbl[lst[i]] = 1 + tbl.get(lst[i], 0)

        # while lst[start] != lst[i] and tbl[lst[i]] > k:
        while (i - start + 1) - max(tbl.values()) > k:
            # shrink the window
            tbl[lst[start]] -= 1

            # move start to right by 1
            start += 1
        
        #calculate the current max lenght
        maxlength = max(maxlength, i - start + 1) #+1 here since we want length not index

    return maxlength

if __name__ == "__main__":
    print(characterReplacement("AAABABB", 1))
    # print(characterReplacement("ABCDE", 1))

