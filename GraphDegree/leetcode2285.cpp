#include <iostream>
#include <vector>
#include <algorithm>

class Solution{
public:
    long long maximumImportance(int n, std::vector<std::vector<int>>& roads) {
        std::vector<int> degree(n, 0);
        const int a = 0, b = 1;
        int res = 0;
        for(std::vector<int> &road : roads){
            degree[road[a]]++;
            degree[road[b]]++;
        }

        std::sort(degree.begin(), degree.end());
        for(int i=0; i < degree.size(); i++){
            res += degree[i] * (i+1);
        }
        return res;
    }
};

int main(){
    long long val;
    int n;
    std::vector<std::vector<int>> roads;

    Solution ans;
    n = 5;
    roads = {{0,1},{1,2},{2,3},{0,2},{1,3},{2,4}};
    val = ans.maximumImportance(n, roads);
    std::cout << "Output: " << val << '\n';

    n = 5;
    roads = {{0,3},{2,4},{1,3}};
    val = ans.maximumImportance(n, roads);
    std::cout << "Output: " << val << '\n';

    return 0;
}