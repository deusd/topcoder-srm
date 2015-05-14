# -*- coding: utf-8 -*-
"""
Problem Statement
    
You are given a tuple (integer) A. An integer K is irreducible with respect to A if K cannot be represented as a sum of one or more elements from A, where each element of A may be used at most once. Return the smallest positive integer that is irreducible with respect to A.
Definition
    
Class:
IrreducibleNumber
Method:
getIrreducible
Parameters:
tuple (integer)
Returns:
integer
Method signature:
def getIrreducible(self, A):

Limits
    
Time limit (s):
2.000
Memory limit (MB):
64
Constraints
-
A will contain between 1 and 3 elements, inclusive.
-
Each element of A will be between 1 and 100, inclusive.
Examples
0)

    
{1,1}
Returns: 3
1 can be expressed as 1, and 2 can be expressed as 1+1.
1)

    
{1,2}
Returns: 4

2)

    
{1,3}
Returns: 2

3)

    
{4, 1, 3}
Returns: 2

This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.
"""

"""
class IrreducibleNumber:
	def getIrreducible(self, A):
		K = 1
		found = False
		A = sorted(A, reverse=True)

		for i in range(len(A) - 1, -1, -1):
			if K == A[i]:
				K += 1
				continue

			theSum = sum(A, i)

			if theSum > K:
				found = True
				break

		if not found:
			K += 1

		return K
"""

class IrreducibleNumber:
	def getIrreducible(self, A):
		S = 0
		K = 0

		A = sorted(A)

		while K < len(A) and A[K] <= S + 1:
			S = S + A[K]
			K = K + 1

		return S + 1

_in = IrreducibleNumber()

print (_in.getIrreducible((1, 1)))
print (_in.getIrreducible((1, 2)))
print (_in.getIrreducible((1, 3)))
print (_in.getIrreducible((4, 1, 3)))


