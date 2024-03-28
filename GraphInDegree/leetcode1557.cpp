#include <iostream>
#include <vector>

class Solution {
public:
    std::vector<int> findSmallestSetOfVertices(int n, std::vector<std::vector<int>>& edges) {
        std::vector<int> res;
        std::vector<int> indegree(n,0);
        const int from = 0, to = 1;

        for(std::vector<int> &edge : edges){
            indegree[edge[to]]++;
        }

        for(int i=0; i < n; i++){
            if(indegree[i] == 0){
                res.push_back(i);
            }
        }
        return res;
    }
};

void print_array(std::vector<int> &val){
    std::cout << "Output: ";
    std::cout << "[";
    for(int i = 0; i < val.size(); i++){
        std::cout << val[i];
        if(i < val.size() - 1){
            std::cout << ", ";
        }
    }
    std::cout << "]";
    std::cout << '\n';
}

int main(){
    int n;
    std::vector<std::vector<int>> edges;
    std::vector<int> res;
    Solution ans;

    n = 6;
    edges = {{0,1},{0,2},{2,5},{3,4},{4,2}};
    res = ans.findSmallestSetOfVertices(n, edges);
    std::cout << "n: " << n << '\n';
    std::cout << "edges: " << "[[0,1],[0,2],[2,5],[3,4],[4,2]]" << '\n';
    print_array(res);
    std::cout << '\n';
    

    n = 5;
    edges = {{0,1},{2,1},{3,1},{1,4},{2,4}};
    res = ans.findSmallestSetOfVertices(n,edges);
    std::cout << "n: " << n << '\n';
    std::cout << "edges: " << "[[0,1],[2,1],[3,1],[1,4],[2,4]]" << '\n';
    print_array(res);
    
    
    edges.clear();
    return 0;

}