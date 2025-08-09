#include <iostream>
#include <vector>
#include <limits>

int main()
{
    int N;
    std::cin >> N;
    std::vector<int> v;
    std::vector<int> min_count_v(N, std::numeric_limits<int>::max());
    min_count_v[0] = 0;

    for(int i=0; i<N; i++)
    {
        int temp;
        std::cin >> temp;
        v.emplace_back(temp);
    }

    for(int i=0; i<N; i++)
    {
        auto max_jump = v[i];
        for(int j=i+1; j<=i+max_jump; j++)
        {
            if(j >= v.size() || min_count_v[i] == std::numeric_limits<int>::max()) break;
            min_count_v[j] = std::min(min_count_v[j], min_count_v[i]+1);
        }
    }

    // for(auto&& i : min_count_v)
    //     std::cout << i;
    if(min_count_v.back() == std::numeric_limits<int>::max()) 
        std::cout << "-1" << std::endl;
    else
        std::cout <<  min_count_v.back() << std::endl;

}