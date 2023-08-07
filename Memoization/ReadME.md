# Memoization

Memoization is a top-down approach to dynamic programming.<br /><br />

The top-down approach is implemented with recursion and made efficient with memoization. To find the n<sup>th</sup> Fibonacci number F(n), F(n-1) + F(n-2) is computed.  This defines the recursive subproblems, and is continued until the base cases are reached.  The problem with just implementing it recursively is that there is a ton of unnecessary repeated computation. <br /><br />

Memoizing a result means to store the result of a function call, usually in a hashmap or an array, so when the function call is repeated, the memoized result is returned instead of recalculated.
