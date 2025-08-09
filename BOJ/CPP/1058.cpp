#include <iostream>
#include <vector>
#include <deque>
#include <array>
#include <list>
#include <tuple>

int bfs(const std::vector<std::vector<int>>& v, std::vector<bool>& visited, int target)
{
    int result = 0;
    std::deque<std::tuple<int, int>> dq; // node, depth 
    visited[target] = true;
    dq.emplace_back(std::make_tuple(target, 0));

    while(!dq.empty())
    {
        auto [node, depth] = dq.front();
        dq.pop_front();
 
        result += 1;

        for(auto&& item : v[node])
        {
            if(!visited[item] && depth+1 <= 2)
            {
                visited[item] = true;
                dq.emplace_back(std::make_tuple(item, depth+1));
            }
        }
    }
    

    return result;

}

int main()
{
    int N;
    int answer = 0;
    std::cin >> N;
    std::vector<std::vector<int>> v;
    v.resize(N); 

    for(int i=0; i<N; i++)
    {
        std::string temp;
        std::cin >> temp;
        for(int j = 0; j < static_cast<int>(temp.size()); j++)
        {
            if(temp[j] == 'Y') v[i].emplace_back(j);
        }
        // temp를 순회하면서, Y인 Index를 v[i]에 push_back
    }

    for(int i=0; i<N; i++)
    {
        std::vector<bool> visited(N, false);

        answer = std::max( bfs(v, visited, i) - 1, answer); // dfs에서 자기자신 제외
    }

    std::cout << answer << std::endl;
}