#include <iostream>
#include <vector>
#include <numeric>


int main()
{
    int N;
    const int64_t LIMIT = 1'000'000'000;
    std::cin >> N;
    std::vector<std::vector<int64_t>> v(N+1, std::vector<int64_t>(11, 0)); // N,자리수 (0~10)

    for(int i=1; i<=N; i++)
    {
        for(int j=0; j<=10; j++)
        {
            if(i == 1 && !(j == 0 || j==10)) // 1이고, 0이나 10아니면 초기화
            {
                v[i][j] = 1;
            }
            else if(i >= 2)
            {
                if(j == 0)
                    v[i][j] = (v[i-1][j+1]) % LIMIT;
                else if(j == 10)
                    continue;
                else
                    v[i][j] = (v[i-1][j-1] + v[i-1][j+1]) % LIMIT;
            }
        }
    }
    
    for (const auto& row : v) {
        for (const auto& elem : row) {
            std::cout << elem << " ";
        }
        std::cout << '\n'; // 한 행 끝나면 줄 바꿈
    }
    int64_t result = std::accumulate(v.back().begin(), v.back().end(), int64_t(0));
    // std::cout << result << std::endl;
    std::cout << result % LIMIT << std::endl;
}