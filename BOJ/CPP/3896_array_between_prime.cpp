
#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>

const std::vector<int> getSortedPrimeNumbers(int start, int end)
{
    std::vector<int> v(end+1);
    std::vector<int> primes;
    std::fill(v.begin(), v.end(), 1); // 순회했을때, 1이면 소수

    for(int i=2; i<static_cast<int>(v.size()); i++)
    {
        if(v[i] == 1) 
            primes.emplace_back(i);
        else 
            continue;

        for(int j=i+i; j<static_cast<int>(v.size()); j=j+i)
        {
            v[j] = 0;
        }
    }

    return primes;
}

int get_answer(const std::vector<int>& primes, int key)
{
    int idx_left  = static_cast<int>(std::lower_bound(primes.begin(), primes.end(), key) - primes.begin());

    if(primes[idx_left] == key) return 0;
    
    // std::cout << primes[idx_left+1] <<  " " <<primes[idx_left-1] << std::endl;
    return primes[idx_left] - primes[idx_left-1];

}

int main()
{
    const auto primes = getSortedPrimeNumbers(1, 1500000);

    // for(auto&& i : primes)
    //     std::cout << i << std::endl;
    int T;
    std::cin >> T;

    for(int i=0; i<T; i++)
    {
        int k;
        std::cin >> k;
        std::cout << get_answer(primes, k) << std::endl;
    }
}