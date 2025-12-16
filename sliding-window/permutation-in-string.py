"""
Permutation in String

You are given two strings s1 and s2.

Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

Both strings only contain lowercase letters.

Example 1:

Input: s1 = "abc", s2 = "lecabee"

Output: true

Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".

Example 2:

Input: s1 = "abc", s2 = "lecaabee"

Output: false

Constraints:

    1 <= s1.length, s2.length <= 1000

"""
def checkInclusion(s1, s2):
    """
    1st try: kind of hard coded solution
    """
    if len(s1) > len(s2):
        return False
        
    l, r = 0, len(s1) - 1
    # i = 0
    
    tbls1 = {}
    
    for chr in s1:
        tbls1[chr] = 1 + tbls1.get(chr, 0)
    
    tbls1_copy = tbls1.copy()
    
    while r < len(s2):
        # i = 0
        # while i < len(s1):
        for _ in range(len(s1)):
            if tbls1.get(s2[l]) != None and tbls1.get(s2[l]) > 0:
                tbls1[s2[l]] -= 1
            # i += 1
            l += 1
                
        if sum(tbls1.values()) == 0:
            return True
            
        tbls1 = tbls1_copy
        tbls1_copy = tbls1.copy()
        
        l -= len(s1)
        l += 1
        r += 1
        
            
    return False


if __name__ == "__main__":
     print(checkInclusion("abc", "abcds"))