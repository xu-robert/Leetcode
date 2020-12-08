'''
Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences.  If multiple answers exist, you may return any of them.

(A string S is a subsequence of string T if deleting some number of characters from T (possibly 0, and the characters are chosen anywhere from T) results in the string S.)

 

Example 1:

Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.
 

Note:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of lowercase English letters.

Solution:
    
This is a twist on the longest common subsequence problem, which is the first section of the
algorithm. The shortest common supersequence is the sequence which preserves the order of 
s1 and s2 as subsequences, with the fewest extra letters possible. If we identify a 
longest common subsequence of s1 and s2, the common sequence will contain letters which
we don't need to duplicate in our supersequence. We can think of it as a sort of "skeleton" 
which we add the rest of s1 and s2 around. For example, lets take "amayoral" and "sarban".

Our LCS has a length of 3, and is "ara". This means the length of our shortest supersequence
would be len(s1) + len(s2) - len(LCS) = 8+6-3=11. An example is "amsAyoRbAnl". where the LCS
is uppercase. How can we prove that the shortest supersequence length is 
len(s1) + len(s2) - len(LCS)? I am not too sure how correct it is, but here is my intuition

say we have "amayoral" and "sarban". The max supersequence we could reasonably build is just
by concantenating the two together: "amayoralsarban" If we want to shorten the supersequence by
one, we need to pick an element that the two strings have in common, like "a". There are multiple
options for which pairs of "a" to choose. But we pick two "a"s and merge the strings to end up
with something like "sAmayoralrban" (where we pick the first a in s1 and s2, and to maintain
the subsequence structure we put everything in S1 before the first a and similar with s2). 
If we want to shorten the supersequence by one again, we need to pick an element that
"mayoral" and "rban" have in common. We could pick "a", which gives us the supersequence "sAmrbAyoraln", at wchich
point we only have two substrings left from s1 and s2: :l and n. So instead of picking a, we 
should pick r, which would give sAmayoRalban. Then we have al and ban, and we can pick a,
leaving sAmayoRbAln. This leaves l and n which dont have any common letters. So we can see
that the pattern is: we pick the longest common subsequence to merge on, and this will
give us the shortest common supersequence. Its not proof at all, but just the intuition. 

So anyway, the algorith itself: first we use our array dp to get k, the length of the LCS.
Then, we work backwards through the dp, according to the rules we used when filling up the dp.
If s1[j] = s2[i], this letter is part of the LCS. Otherwise, we either shift i or j. Everytime
we identify a member of the LCS, we decrement k and add the current (i,j) to a stack. When
we hit k = 0, we found the last element of our lcs and our stack has the (i,j) indices of our
LCS in reverse order (first index of LCS on top of stack)

So we just pop off from the stack to get i,j. s1[j] = s2[i], and all elements s1[:j] and s2[:i]
need to go before s1[j] in our supersequence to ensure that s1 and s2 are subsequences of the
supersequence. Then we store i+1,j+1 as last indices, and when we pop off from the stack again,
we place s1[last_j:cur_j] and s2[last_i:cur_i] before placing s1[cur_i] etc..til the end

'''
class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        dp = [[0 for _ in range(len(str1)+1)] for _ in range(len(str2)+1)]
        
        for i in range(len(str2)):
            for j in range(len(str1)):
                if str1[j] == str2[i]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        
        common_indices = []
        i = len(dp)-1
        j = len(dp[0])-1
        k = dp[-1][-1]
        while k > 0:
            if str1[j-1] == str2[i-1]:
                common_indices.append([i-1, j-1])
                k -= 1
                i -= 1
                j -= 1
            elif dp[i][j] == dp[i-1][j]:
                i -= 1
            elif dp[i][j] == dp[i][j-1]:
                j -= 1
        
        ans = ''
        
        str1_last, str2_last = 0, 0
        while common_indices:
            str2_idx, str1_idx = common_indices.pop()
            ans += str1[str1_last:str1_idx]
            ans += str2[str2_last:str2_idx]
            ans += str1[str1_idx]
            str1_last, str2_last = str1_idx+1, str2_idx+1
        
        ans += str1[str1_last:]
        ans += str2[str2_last:]
        return ans
    
a = Solution()
b = a.shortestCommonSupersequence('milk', 'milk')