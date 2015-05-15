"""
Problem Statement for DecipherabilityEasy


Problem Statement
    	You had a non-empty string s but you lost it. Cat Snuke found the string and removed one character from the string. Later, Snuke gave you the string t. Can this be the string created from your string s?



You are given the Strings s and t. Return "Possible" (quotes for clarity) if t can be obtained from s by erasing exactly one character. Otherwise, return "Impossible". Note that the return value is case-sensitive.
 
Definition
    	
Class:	DecipherabilityEasy
Method:	check
Parameters:	String, String
Returns:	String
Method signature:	String check(String s, String t)
(be sure your method is public)
    
 
Constraints
-	The number of characters in s will be between 1 and 50, inclusive.
-	Every character in s will be a lowercase letter ('a'-'z').
-	The number of characters in t will be between 1 and 50, inclusive.
-	Every character in t will be a lowercase letter ('a'-'z').
 
Examples
0)	
    	
"sunuke"
"snuke"
Returns: "Possible"
If Cat Snuke erase the first 'u' from s, it will equal to t.
1)	
    	
"snuke"
"skue"
Returns: "Impossible"
Swapping characters is not allowed.
2)	
    	
"snuke"
"snuke"
Returns: "Impossible"
Erasing nothing is not allowed.
3)	
    	
"snukent"
"snuke"
Returns: "Impossible"
Cat Snuke can erase exactly one character.
4)	
    	
"aaaaa"
"aaaa"
Returns: "Possible"
5)	
    	
"aaaaa"
"aaa"
Returns: "Impossible"
6)	
    	
"topcoder"
"tpcoder"
Returns: "Possible"
7)	
    	
"singleroundmatch"
"singeroundmatc"
Returns: "Impossible"
This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2010, TopCoder, Inc. All rights reserved.




This problem was used for: 
       Single Round Match 649 Round 1 - Division II, Level One
"""

# first attempt
# class DecipherabilityEasy:
# 	def check(self, s, t):
# 		true = "Possible"
# 		false = "Impossible"
# 		count = 0

# 		if len(t) >= len(s): return false
# 		elif len(s) - len(t) > 1: return false
# 		for i in range(len(t)):
# 			print ("%s, %s" % (s[i + count], t[i]))
# 			if s[i + count] != t[i]:
# 				count += 1
# 				if count > 1 or s[i + count] != t[i]:
# 					print ("%s, %s" % (s[i + count], t[i]))
# 					return false

# 		return true

# second attempt - optimal solution
class DecipherabilityEasy:
	def check(self, s, t):
		for i in range(len(s)):
			if s[:i] + s[i + 1:] == t:
				return "Possible"

		return "Impossible"

de = DecipherabilityEasy()


print de.check("sunuke", "snuke")
# Returns: "Possible"
    	
print de.check("snuke", "skue")
# Returns: "Impossible"
    	
print de.check("snuke", "snuke")
# Returns: "Impossible"
    	
print de.check("snukent", "snuke")
# Returns: "Impossible"
    	
print de.check("aaaaa", "aaaa")
# Returns: "Possible"	
    	
print de.check("aaaaa", "aaa")
# Returns: "Impossible"	
    	
print de.check("topcoder", "tpcoder")
# Returns: "Possible"	
