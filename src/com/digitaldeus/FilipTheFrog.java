package com.digitaldeus;

/**
 * Created by deusduke on 5/12/15.
 *
 *
 Problem Statement
     
 Filip the Frog lives on a number line. There are islands at some points on the number line. You are given the positions of these islands in the int[] positions.  Filip starts on the island located at positions[0]. His maximal jump length is L, which means that he can jump to any island that is within a distance of L (inclusive) from his current location. Filip can't jump to a point on the number line that doesn't contain an island. He can make an unlimited number of jumps.  An island is reachable if Filip can get to it through some sequence of jumps. Please find and return the number of reachable islands.
 Definition
     
 Class:
 FilipTheFrog
 Method:
 countReachableIslands
 Parameters:
 int[], int
 Returns:
 int
 Method signature:
 int countReachableIslands(int[] positions, int L)
 (be sure your method is public)
 Limits
     
 Time limit (s):
 2.000
 Memory limit (MB):
 256
 Stack limit (MB):
 256
 Notes
 -
 If two islands are located at points A and B on the number line, then the distance between them is |A - B|.
 Constraints
 -
 positions will contain between 1 and 50 elements, inclusive.
 -
 Each element of positions will be between 0 and 1000, inclusive.
 -
 The elements of positions will be distinct.
 -
 L will be between 1 and 1000, inclusive.
 Examples
 0)

     
 {4, 7, 1, 3, 5}
 1
 Returns: 3
 Filip starts at position 4 and his maximal jump length is 1. He can reach the islands at positions 3, 4, and 5.
 1)

     
 {100, 101, 103, 105, 107}
 2
 Returns: 5
 Here he can reach all 5 islands.
 2)

     
 {17, 10, 22, 14, 6, 1, 2, 3}
 4
 Returns: 7

 3)

     
 {0}
 1000
 Returns: 1

 This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.
 *
 */

import java.util.Arrays;
public class FilipTheFrog {

    // first attempt
//    public static int countReachableIslands(int[] positions, int L) {
//        int islands = 0;
//        boolean[] canReach = new boolean[positions.length];
//
//        canReach[0] = true;
//        for (int i = 0; i < positions.length - 1; ++i)
//            for (int j = i + 1; j < positions.length; ++j)
//                if (Math.abs(positions[i] - positions[j]) <= L) {
//                    canReach[i] = true;
//                    canReach[j] = true;
//                }
//
//        for (boolean reachable : canReach ) {
//            if (reachable) ++islands;
//        }
//
//        return islands;
//    }


    // second attempt
//    public static int countReachableIslands(int[] positions, int L) {
//        int islands = 0;
//
//        boolean[] canReach = new boolean[positions.length];
//        canReach[0] = true;
//        for (int i = 0; i < positions.length - 1; ++i)
//            for (int j = i + 1; j < positions.length; ++j)
//                if (Math.abs(positions[i] - positions[j]) <= L) {
//                    canReach[i] = true;
//                    canReach[j] = true;
//                }
//
//        for (boolean reachable : canReach)
//            if (reachable)
//                ++islands;
//        return islands;
//    }


    // second attempt
    public static int countReachableIslands(int[] positions, int L) {
        if (positions == null || positions.length == 0) return 0;

        int islands = 0;

        boolean[] canReach = new boolean[positions.length];
        canReach[0] = true;
        for (int i = 0; i < positions.length - 1; ++i)
            for (int j = i + 1; j < positions.length; ++j)
                if (Math.abs(positions[i] - positions[j]) <= L) {
                    canReach[i] = true;
                    canReach[j] = true;
                }

        for (boolean reachable : canReach)
            if (reachable)
                ++islands;
        return islands;
    }

    public static void main(String args[]) {
        // should be 3
        System.out.println(FilipTheFrog.countReachableIslands(new int[]{4, 7, 1, 3, 5}, 1));

        // should be 5
        System.out.println(FilipTheFrog.countReachableIslands(new int[]{100, 101, 103, 105, 107}, 2));

        // should be 7
        System.out.println(FilipTheFrog.countReachableIslands(new int[] {17, 10, 22, 14, 6, 1, 2, 3}, 4));

        // should be 1
        System.out.println(FilipTheFrog.countReachableIslands(new int[] {0}, 1000));
    }
}
