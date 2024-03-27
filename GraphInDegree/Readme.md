# Graph InDegree

A graph is a set of vertices, nodes, and edges between select pairs of vertices.  Thus, G = (V,E), a graph is an unordered set of vertices and an unordered collection of, vertex pairs, edges.  Graphs are generally drawn with circles for vertices and lines connecting vertices for the edges.  
<br/><br/>

Undirected graphs have undirected edges.  Thus an edge between u and v, e = {u, v}, have a symmetric relation.  This symmetric relation means {u, v} = {v, u}.  Graphs that depict relations that do not have this reciprocity are directed graphs.  In directed graphs, e = {u, v}, the edge points from the first vertex in the pair and points to the second vertex in the pair.  
<br/><br/>

In undirected graphs when there is an edge connecting two vertices, the vertices are adjacent to one another.  Thus an edge in an undirected graph is incident to the vertices the edge connects.  The degree of a vertex in an undirected graph is the number of edges incident to the vertex.  The outdegree of a vertex in a directed graph is the number of edges going from the vertex.  The indegree of a vertex is the number of edges going to the vertex.
<br/><br/>

Lets look at an example... <br/>
## LeetCode1557 

Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [from<sub>i<sub/>, to<sub>i<sub/>] represents a directed edge from node from<sub>i<sub/> to node to<sub>i<sub/>.  Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique solution exists.  Notice that you can return the vertices in any order.
<br/><br/>

Solution...
If there is an indegree to a vertex, that vertex will be reached without manually visiting the vertex.  
<br/><br/>

Correctness...
1.  Each of the n vertices are assumed to not have edges, so the n vertices are initialized as not having an indegree.  
2.  Iterate through the edges, and the indegree is set to true for all edges with an indegree.
3.  Iterate through the n vertices, and store vertices without an indegree into results.

See photo for code in Output.


Resources... <br/>
[1] Dasgupta, S., Papadimitriou, C.H., Vazirani, U.V. (2006). Algorithms New York, McGraw-Hill Education <br/>
[2] Sedgewick, R., Wayne, K. (2011). Algorithms 4th ed. New York, Addison-Wesley <br/>
[3] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C. (2009) Introduction to algorithms 3rd ed. Massachusetts, MIT Press <br/>
