// Red Black Tree
// or
// heap + search?

#include <iostream>
#include <vector>
#include <set>
#include <fstream>

static void pushMiddleNumber(std::multiset<int>& ms, std::vector<int>& answer)
{
    // 중앙값 구하기 
    auto slow = ms.begin();
    auto fast = ++ms.begin();

    while(fast != ms.end())
    {
        // std::cout << *slow << " " << *fast << std::endl;
        ++slow;
        ++(++fast);
    }

    // std::cout << "넣기" << std::endl;
    answer.push_back(*(slow));
    return;

}

int main()
{
    // std::ifstream ifs;
    // ifs.open("2696.in");

    int T;
    std::cin >> T;

    for(int i=0; i<T; i++)
    {
        int M;
        int count = 0;
        std::multiset<int> ms;
        std::vector<int> answer;
        std::cin >> M;
        for(int j=0; j<M; j++)
        {
            int temp;
            std::cin >> temp;
            ms.insert(temp);

            if((++count) % 2 == 1) 
                pushMiddleNumber(ms, answer); // 중앙값 구해서 넣기

        }


        int print_count = 0;
        std::cout << static_cast<int>(answer.size()) << std::endl;
        for(int j=0; j<static_cast<int>(answer.size()); j++)
        {
            std::cout << answer[j] << " ";

            if((++print_count) == 10 || j == static_cast<int>(answer.size()) - 1)
                std::cout << "\n";
        }
    }
}