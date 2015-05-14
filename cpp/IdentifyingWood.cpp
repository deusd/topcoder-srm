#include "IdentifyingWood.h"
using namespace std;

string IdentifyingWood::check(string s, string t) {
    int j = 0;
    for (int i = 0; i < s.length() && j < t.length(); ++i) {
        if (s[i] == t[j]) ++j;
    }

    return j == t.length() ? "Yep, it's wood." : "Nope.";
}
