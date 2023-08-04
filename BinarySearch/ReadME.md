# Binary Search

The binary search algorithm uses repeated subdivision of the data.  This makes binary search a divide-and-conquer algorithm. <br /><br />  

The recurrence is T(n) = T($\lceil n/2 \rceil$) + O(1). Plugging a = 1, b = 2, d = 0 into the following master theorem gives a running time of just O(log n)
Master Theorem:  O(n<sup>d</sup> log n) if d == log<sub>b</sub>a.  


