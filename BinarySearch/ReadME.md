# Binary Search

The binary search algorithm uses repeated subdivision of the data.  This makes binary search a divide-and-conquer algorithm. <br /><br />  

The recurrence is T(n) = T(ceiling(n/2)) + O(1). Plugging a = 1, b = 2, d = 0 into the following master theorem gives a running time of just O(log n)
Master Theorem:  O(n**d log n) if d == log (base b) a.  

\lceil x \rceil
