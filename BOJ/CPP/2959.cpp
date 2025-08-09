#include <iostream>
#include <vector>
#include <limits>
#include <set>


int get_result(const std::vector<int>& v, const int a, const int b)
{
    int cur_min = std::numeric_limits<int>::max();
    for (int i=0; i < static_cast<int>(v.size()); i++)
    {
        if(i == a || i == b)
            continue;

        cur_min = std::min(cur_min, v[i]);
    }

    
    return std::min(v[a], v[b]) * cur_min;

}
int main()
{
    std::vector<int> v;
    int answer = std::numeric_limits<int>::min();
    
    for(int i=0; i<4; i++)
    {
        int temp = 0;
        std::cin >> temp;
        v.emplace_back(temp);
    }
    
    for(int i = 0; i<v.size() - 1; i++)
    {
        for(int j = i+1; j<v.size(); j++)
        {
            answer = std::max(get_result(v, i, j), answer);
        }
    }
    
    std::cout << answer << std::endl;


}