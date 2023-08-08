# Decode Ways

A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1" <br />
'B' -> "2" <br />
... <br />
'Z' -> "26" <br /><br />
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:<br /><br />

"AAJF" with the grouping (1 1 10 6) <br />
"KJF" with the grouping (11 10 6) <br />
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06". <br /><br />

Given a string s containing only digits, return the number of ways to decode it.
