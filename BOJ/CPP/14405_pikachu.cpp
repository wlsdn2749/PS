#include <iostream>
#include <set>
#include <ranges>

bool bIsPikachu(std::string inputString)
{
    std::set<std::string> canSayWords = {"pi", "ka", "chu"};

    // inputString을 돌면서, canSayWords에 해당하지 않는 문자열의 경우 False, 아닌 경우 True
    for(auto it = inputString.begin(); it != inputString.end(); )
    {
        auto result = [&]() 
        {
            for(auto&& word : canSayWords)
            {
                // std::cout << std::string (it, it + word.size()) << " vs " << word << std::endl;
                if(std::string (it, it + word.size()) == word)
                {
                    it += word.size();
                    return true;
                }
            }
            return false;
        };
        
        if (result())
            continue;
        else
            return false;
    }

    return true;
}

int main()
{
    std::string input;
    std::cin >> input;

    if(bIsPikachu(input))
    {
        std::cout << "YES" << std::endl;
    }
    else
    {
        std::cout << "NO" << std::endl;
    }
}