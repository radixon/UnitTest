# Undirected Graph algorithms' Degree explained

Undirected graphs have undirected edges.  Thus an edge between u and v, e = {u, v}, have a symmetric relation.  This symmetric relation means {u, v} = {v, u}.  
<br /><br />

Two node are neighbors or adjacent if there is an edge between the nodes.  The degree of a node is the node's number of neighbors.  The sum of degrees in a graph is always twice the number of edges due to each edge increasing the degree of exactly two nodes by one.
<br /><br />

## LeetCode2285

You are given an integer n denoting the number of cities in a country. The cities are numbered from 0 to n - 1.  You are also given a 2D integer array roads where roads[i] = [ai, bi] denotes that there exists a bidirectional road connecting cities ai and bi.
<br /><br />

You need to assign each city with an integer value from 1 to n, where each value can only be used once. The importance of a road is then defined as the sum of the values of the two cities it connects.  Return the maximum total importance of all roads possible after assigning the values optimally.
<br /><br />

Solution...
1.  Count the degree of each node (city).
2.  Sort the nodes in ascending order by degree.
3.  Multiply the degree by the degree by the level of importance, and add to the result.
<br /><br />

Correctness... <br />
The variable that will hold the result is initialized and the array that will retain the degree is initialized.  In C++, a vector can be initialized as follows: <br />
vector<type> variableName(number_of_elements, value_to_initialize_elements)
<br /><br />

The vector is initialized with n elements and a value of 0.
<br /><br />
Iterate through roads.  Increment the degree of the node as the node appears in roads.
<br /><br />
Sort the vector in ascending order.  Add the degree of the node multiplied by the importance of the node to the results variable.
<br /><br />
return the results variable.
<br /><br />

![leetcode2285](https://github.com/radixon/UnitTest/assets/59415488/a01d148b-ef2a-45e0-aecf-50d84a5f743e)


Resources
[1]  Laaksonen, Antti (2017). Competitive programmer's handbook. Springer.
[2] Dasgupta, S., Papadimitriou, C.H., Vazirani, U.V. (2006). Algorithms New York, McGraw-Hill Education
