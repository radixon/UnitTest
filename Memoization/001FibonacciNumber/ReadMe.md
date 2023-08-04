# Fibonacci Number

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

# Intuition

The Fibonacci Number is a foundational problem explained in many computer science textbooks.  The rate at which it grows, allows for an exploration into the importance of memoization.  Without memoization, the running time of the recursive solution to the Fibonacci number is exponential in n.  To calculate fib(200) recursively, without memoization, would take approximately 2<sup>92</sup> seconds.  Using memoization, this problem becomes linear in n.


# Resources

Sanjoy Dasgupta, Christos papadimitriou, Umesh Vazirani, *Algorithms.* NY, New York: McGraw-Hill, 2008.
