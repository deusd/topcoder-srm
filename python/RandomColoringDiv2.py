# -*- coding: utf-8 -*-
"""
Problem Statement
    
Little Arthur has a new frisbee and he would like to color it. A frisbee has the shape of a disc. Arthur will color the disc using two colors: one for the top side, one for the bottom side.  Each color is defined by three integer components: R, G, and B (meaning red, green, and blue, respectively), where 0 <= R < maxR, 0 <= G < maxG, and 0 <= B < maxB. It is known that Arthur can use any of the maxR*maxG*maxB possible colors.  Arthur is going to perform the coloring in the following way:
In the first step, he will color the top side of the frisbee using the color (startR, startG, startB).
In the second step, he will color the bottom side of the frisbee using a color that makes a good transition from the first color. (This is explained below.)
 A transition from color (R, G, B) to color (R', G', B') is called good if all components differ by at most d2 units (formally, |R - R'| <= d2, |G - G'| <= d2, |B - B'| <= d2) and at least one component differs by at least d1 units (formally, at least one of the conditions |R - R'| >= d1, |G - G'| >= d1, |B - B'| >= d1 holds). Intuitively, a transition between two colors is called good if they are neither too similar, nor too different.  After coloring the top side Arthur is wondering how many different options there are now for the color of the bottom side of the frisbee.  Given integers maxR, maxG, maxB, startR, startG, startB, d1, and d2, return the number of valid colors that make a good transition from the color (startR, startG, startB).
Definition
    
Class:
RandomColoringDiv2
Method:
getCount
Parameters:
integer, integer, integer, integer, integer, integer, integer, integer
Returns:
integer
Method signature:
def getCount(self, maxR, maxG, maxB, startR, startG, startB, d1, d2):

Limits
    
Time limit (s):
2.000
Memory limit (MB):
64
Constraints
-
maxR, maxG and maxB will each be between 1 and 100, inclusive.
-
startR will be between 0 and maxR-1, inclusive.
-
startG will be between 0 and maxG-1, inclusive.
-
startB will be between 0 and maxB-1, inclusive.
-
d1 and d2 will each be between 0 and 100, inclusive.
-
d1 will be less than or equal to d2.
Examples
0)

    
5
1
1
2
0
0
0
1
Returns: 3
Only the R component can change here. It has to change by at least 0 and at most 1. Thus the colors that make a good transition from color (2, 0, 0) here are (1, 0, 0), (2, 0, 0), and (3, 0, 0).
1)

    
4
2
2
0
0
0
3
3
Returns: 4
Colors that make a good transition from color (0, 0, 0) here are (3, 0, 0), (3, 0, 1), (3, 1, 0), and (3, 1, 1).
2)

    
4
2
2
0
0
0
5
5
Returns: 0
At least one component has to change by 5. There exists no color that makes a good transition from color (0, 0, 0) within the respective maxR, maxG, maxB constraints.
3)

    
6
9
10
1
2
3
0
10
Returns: 540
All valid colors make a good transition from color (1, 2, 3).
4)

    
6
9
10
1
2
3
4
10
Returns: 330

5)

    
49
59
53
12
23
13
11
22
Returns: 47439

This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.
"""


class RandomColoringDiv2:
    @staticmethod
    def getCount(maxR, maxG, maxB, startR, startG, startB, d1, d2):
        T = 0

        d = d2
        for r in range(startR - d, startR + d + 1):
            if 0 <= r < maxR: 
                for g in range(startG - d, startG + d + 1):
                    if 0 <= g < maxG: 
                        for b in range(startB - d, startB + d + 1):
                            if 0 <= b < maxB:
                                if abs(r - startR) >= d1 or abs(g - startG) >= d1 or abs(b - startB) >= d1:
                                    T += 1

        return T

# print (RandomColoringDiv2.getCount(5, 1, 1, 2, 0, 0, 0, 1)) # 3
# print (RandomColoringDiv2.getCount(4, 2, 2, 0, 0, 0, 3, 3)) # 4
# print (RandomColoringDiv2.getCount(4, 2, 2, 0, 0, 0, 5, 5)) # 0
print (RandomColoringDiv2.getCount(6, 9, 10, 1, 2, 3, 0, 10)) # 540

