package com.digitaldeus;


/**
 *
 Problem Statement
 We call a pair of s (s, t) "wood" if t is contained in s as a subsequence. (See Notes for a formal definition.)


 Given s s and t, return the "Yep, it's wood." (quotes for clarity) if the pair (s, t) is wood and "Nope." otherwise.

 Definition
 Class: IdentifyingWood
 Method: check
 Parameters: String, String
 Returns: String
 Method signature: String check(String s, String t)
 (be sure your method is public)
 Limits
 Time limit (s): 2.000
 Memory limit (MB): 256
 Notes
 - String t is contained in string s as a subsequence if we can obtain t by removing zero or more (not necessarily consecutive) characters from s.
 Constraints
 - s and t will consist only of lowercase English letters.
 - s and t will each be between 1 and 10 characters long, inclusive.
 Examples
 0)
 "absdefgh"
 "asdf"
 Returns: "Yep, it's wood."
 1)
 "oxoxoxox"
 "ooxxoo"
 Returns: "Nope."
 2)
 "oxoxoxox"
 "xxx"
 Returns: "Yep, it's wood."
 3)
 "qwerty"
 "qwerty"
 Returns: "Yep, it's wood."
 4)
 "string"
 "longstring"
 Returns: "Nope."
 This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved
 */

import java.lang.System;

public class IdentifyingWood {
    public static String check(String s, String t) {
        int foundChars = 0;
        for (int i = 0; i < s.length() && foundChars < t.length(); ++i) {
            if (s.charAt(i) == t.charAt(foundChars)) {
                ++foundChars;
            }
        }

        if (foundChars == t.length())
            return "Yep, it's wood.";
        else
            return "Nope.";
    }

    public static void main (String[] args) {
//        Examples
//        0)
//        "absdefgh"
//        "asdf"
//        Returns: "Yep, it's wood."
//        1)
//        "oxoxoxox"
//        "ooxxoo"
//        Returns: "Nope."
//        2)
//        "oxoxoxox"
//        "xxx"
//        Returns: "Yep, it's wood."
//        3)
//        "qwerty"
//        "qwerty"
//        Returns: "Yep, it's wood."
//        4)
//        "string"
//        "longstring"
//        Returns: "Nope."


        // Returns: "Yep, it's wood."
        System.out.println(IdentifyingWood.check("absdefgh", "asdf"));
    }
}